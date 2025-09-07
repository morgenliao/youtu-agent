import json
import pathlib
import re

from ...config import AgentConfig
from ...utils import SimplifiedAsyncOpenAI, get_jinja_env
from .common import AgentInfo, CreatePlanResult, OrchestraTaskRecorder, Subtask


class OutputParser:
    """输出解析器，用于解析规划代理的输出文本。

    该类负责从LLM的输出中提取分析内容和任务计划。
    """

    def __init__(self):
        """初始化输出解析器。

        设置用于匹配分析和计划内容的正则表达式模式。
        """
        self.analysis_pattern = r"<analysis>(.*?)</analysis>"
        self.plan_pattern = r"<plan>\s*\[(.*?)\]\s*</plan>"
        # self.next_step_pattern = r'<next_step>\s*<agent>\s*(.*?)\s*</agent>\s*<task>\s*(.*?)\s*</task>\s*</next_step>'
        # self.task_finished_pattern = r'<task_finished>\s*</task_finished>'

    def parse(self, output_text: str) -> CreatePlanResult:
        """解析输出文本并返回规划结果。

        从LLM的输出中提取分析内容和任务计划。

        Args:
            output_text: LLM生成的输出文本。

        Returns:
            CreatePlanResult: 包含分析和任务列表的规划结果。
        """
        analysis = self._extract_analysis(output_text)
        plan = self._extract_plan(output_text)
        return CreatePlanResult(analysis=analysis, todo=plan)

    def _extract_analysis(self, text: str) -> str:
        """从文本中提取分析内容。

        使用正则表达式匹配<analysis>标签内的内容。

        Args:
            text: 包含分析内容的文本。

        Returns:
            str: 提取的分析内容，如果未找到则返回空字符串。
        """
        match = re.search(self.analysis_pattern, text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return ""

    def _extract_plan(self, text: str) -> list[Subtask]:
        """从文本中提取任务计划。

        使用正则表达式匹配<plan>标签内的JSON格式任务列表。

        Args:
            text: 包含任务计划的文本。

        Returns:
            list[Subtask]: 提取的任务列表。
        """
        match = re.search(self.plan_pattern, text, re.DOTALL)
        if not match:
            return []
        plan_content = match.group(1).strip()
        tasks = []
        task_pattern = r'\{"agent_name":\s*"([^"]+)",\s*"task":\s*"([^"]+)",\s*"completed":\s*(true|false)\s*\}'
        task_matches = re.findall(task_pattern, plan_content, re.IGNORECASE)
        for agent_name, task_desc, completed_str in task_matches:
            completed = completed_str.lower() == "true"
            tasks.append(Subtask(agent_name=agent_name, task=task_desc, completed=completed))
        return tasks


class PlannerAgent:
    """规划代理，用于生成任务执行计划。

    该类负责根据用户任务和可用代理信息，使用LLM生成详细的执行计划。
    """

    def __init__(self, config: AgentConfig):
        """初始化规划代理。

        Args:
            config: 代理配置对象，包含模型和规划相关设置。
        """
        self.config = config
        self.llm = SimplifiedAsyncOpenAI(**self.config.planner_model.model_provider.model_dump())
        self.output_parser = OutputParser()
        self.jinja_env = get_jinja_env(str(pathlib.Path(__file__).parent / "prompts"))
        self.planner_examples = self._load_planner_examples()
        self.available_agents = self._load_available_agents()

    @property
    def name(self) -> str:
        """获取代理名称。

        Returns:
            str: 代理名称，默认为"planner"。
        """
        return self.config.planner_config.get("name", "planner")

    def _load_planner_examples(self) -> list[dict]:
        """加载规划示例数据。

        从配置文件指定的路径或默认路径加载JSON格式的规划示例。

        Returns:
            list[dict]: 规划示例列表。
        """
        examples_path = self.config.planner_config.get("examples_path", "")
        if examples_path and pathlib.Path(examples_path).exists():
            examples_path = pathlib.Path(examples_path)
        else:
            examples_path = pathlib.Path(__file__).parent / "data" / "planner_examples.json"
        with open(examples_path, encoding="utf-8") as f:
            return json.load(f)

    def _load_available_agents(self) -> list[AgentInfo]:
        """加载可用代理信息。

        从配置中获取所有工作代理的信息。

        Returns:
            list[AgentInfo]: 可用代理信息列表。
        """
        available_agents = []
        for info in self.config.workers_info:
            available_agents.append(AgentInfo(**info))
        return available_agents

    async def build(self):
        """构建代理。

        当前实现为空，预留用于未来扩展。
        """
        pass

    async def create_plan(self, task_recorder: OrchestraTaskRecorder) -> CreatePlanResult:
        """创建任务执行计划。

        使用LLM根据任务记录器生成详细的执行计划，包括分析和子任务列表。

        Args:
            task_recorder: 包含任务信息的记录器对象。

        Returns:
            CreatePlanResult: 包含分析和任务列表的规划结果。
        """
        sp = self.jinja_env.get_template("planner_sp.j2").render(
            planning_examples=self._format_planner_examples(self.planner_examples)
        )
        up = self.jinja_env.get_template("planner_up.j2").render(
            available_agents=self._format_available_agents(self.available_agents),
            question=task_recorder.task,
            background_info="",  # TODO: add background info?
        )
        messages = [{"role": "system", "content": sp}, {"role": "user", "content": up}]
        response = await self.llm.query_one(messages=messages, **self.config.planner_model.model_params.model_dump())
        return self.output_parser.parse(response)

    def _format_planner_examples(self, examples: list[dict]) -> str:
        """格式化规划示例为字符串。

        将示例字典列表转换为适合LLM提示的字符串格式。

        Args:
            examples: 规划示例字典列表。

        Returns:
            str: 格式化后的示例字符串。
        """
        # format examples to string. example: {question, available_agents, analysis, plan}
        examples_str = []
        for example in examples:
            examples_str.append(
                f"Question: {example['question']}\n"
                f"Available Agents: {example['available_agents']}\n\n"
                f"<analysis>{example['analysis']}</analysis>\n"
                f"<plan>{json.dumps(example['plan'], ensure_ascii=False)}</plan>\n"
            )
        return "\n".join(examples_str)

    def _format_available_agents(self, agents: list[AgentInfo]) -> str:
        """格式化可用代理信息为字符串。

        将代理信息列表转换为适合LLM提示的字符串格式。

        Args:
            agents: 可用代理信息列表。

        Returns:
            str: 格式化后的代理信息字符串。
        """
        agents_str = []
        for agent in agents:
            agents_str.append(
                f"- {agent.name}: {agent.desc}\n  Best for: {agent.strengths}\n"
                if agent.strengths
                else f"  Weaknesses: {agent.weaknesses}\n"
                if agent.weaknesses
                else ""
            )
        return "\n".join(agents_str)
