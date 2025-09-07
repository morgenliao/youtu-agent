import pathlib
import re

from utu.agents.orchestra.common import CreatePlanResult, OrchestraTaskRecorder
from utu.agents.orchestra.planner import PlannerAgent
from utu.config import AgentConfig
from utu.tools import TabularDataToolkit
from utu.utils import get_jinja_env

"""数据分析规划代理模块。

此模块定义了 DAPlannerAgent 类，用于数据分析任务的规划。
"""


class DAPlannerAgent(PlannerAgent):
    """数据分析规划代理。

    该类继承自 PlannerAgent，专门用于数据分析任务的规划，
    能够从任务描述中提取文件路径并获取表格数据列信息。
    """

    def __init__(self, config: AgentConfig):

        """初始化数据分析规划代理。

        Args:
            config: 代理配置对象。
        """

        super().__init__(config)

        self.jinja_env = get_jinja_env(

            str(pathlib.Path(__file__).parent.parent.parent / "utu" / "agents" / "orchestra" / "prompts")

        )

    async def create_plan(self, task_recorder: OrchestraTaskRecorder) -> CreatePlanResult:

        """创建规划。

        根据任务记录器创建规划，包括获取背景信息、渲染模板等。

        Args:
            task_recorder: 管弦乐任务记录器。

        Returns:
            CreatePlanResult: 规划结果。
        """

        background_info = await self._get_background_info(task_recorder)
        sp = self.jinja_env.get_template("planner_sp.j2").render(
            planning_examples=self._format_planner_examples(self.planner_examples)
        )
        up = self.jinja_env.get_template("planner_up.j2").render(
            available_agents=self._format_available_agents(self.available_agents),
            question=task_recorder.task,
            background_info=background_info,
        )
        messages = [{"role": "system", "content": sp}, {"role": "user", "content": up}]
        response = await self.llm.query_one(messages=messages, **self.config.planner_model.model_params.model_dump())
        return self.output_parser.parse(response)

    async def _get_background_info(self, task_recorder: OrchestraTaskRecorder) -> str:
        """获取背景信息。

        从任务记录器中获取表格列信息。

        Args:
            task_recorder: 管弦乐任务记录器。

        Returns:
            str: 背景信息字符串。
        """
        data_analysis_tool = TabularDataToolkit()
        file_path = self._extract_file_path(task_recorder.task)
        if not file_path:
            return ""
        columns_info = await data_analysis_tool.get_column_info(file_path)
        info_str = f"Data columns of `{file_path}`:\n{columns_info}" if columns_info else ""
        info_str += (
            "\n**Note**: These background information is invisible to other agents, "
            "but can help you to make better plan. So your plan should be based on the assumption "
            "that the agents is initially unaware of this information."
        )
        return info_str

    def _extract_file_path(self, task: str) -> str:
        """从任务描述中提取文件路径。

        使用正则表达式从任务字符串中提取被反引号包围的文件路径。

        Args:
            task: 任务描述字符串。

        Returns:
            str: 提取的文件路径，如果未找到则返回空字符串。
        """
        match = re.search(r"`([^`]+)`", task)
        if match:
            return match.group(1).strip()
        return ""
