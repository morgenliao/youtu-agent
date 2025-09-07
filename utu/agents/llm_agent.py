"""LLM 代理实现模块。

该模块提供了将底层模型封装为代理的简单实现 `LLMAgent`，用于同步或流式地
调用模型并收集执行记录。Docstrings 使用 Google 风格：首行简短总结，随后空行
再给出更详细说明；标题（Args/Returns/Raises）保留英文，具体说明为中文。
"""

from agents import Agent, Runner, RunResultStreaming, TResponseInputItem, trace

from ..config import ModelConfigs
from ..utils import AgentsUtils, get_logger
from .base_agent import BaseAgent
from .common import TaskRecorder

logger = get_logger(__name__)


class LLMAgent(BaseAgent):
    """封装具体模型的最小代理实现。

    该代理将 `agents` 库中的模型适配为 `BaseAgent` 接口，可同步调用（`run`）
    或以流式方式调用（`run_streamed`）。构造时接收 `ModelConfigs` 来配置模型。
    """

    def __init__(self, config: ModelConfigs):
        """初始化 LLMAgent 并构建内部 Agent 实例。

        Args:
            config: 包含模型提供者、模型设置等信息的配置对象 `ModelConfigs`。

        Returns:
            None
        """
        self.config = config
        self.agent = Agent(
            name="LLMAgent",
            model=AgentsUtils.get_agents_model(**config.model_provider.model_dump()),
            model_settings=config.model_settings,
            # tools=config.tools,
            # output_type=config.output_type,
        )

    def set_instructions(self, instructions: str):
        """设置代理的指令（instructions）。

        Args:
            instructions: 要传给底层 agent 的指令文本。

        Returns:
            None
        """
        self.agent.instructions = instructions

    async def run(self, input: str | list[TResponseInputItem], trace_id: str | None = None, **kwargs) -> TaskRecorder:
        """执行一次完整的（非流式）任务并返回任务记录器。

        Args:
            input: 要发送给模型的输入，既可以是字符串，也可以是 `TResponseInputItem` 列表，
                具体格式依底层 agent 要求而定。
            trace_id: 可选的链路跟踪 ID；若未提供将自动生成并用于 trace 上下文。

        Returns:
            TaskRecorder: 包含运行结果、最终输出及相关元数据的记录对象。
        """
        trace_id = trace_id or AgentsUtils.gen_trace_id()
        # 将 task 字段统一为字符串以匹配 TaskRecorder 的类型定义
        task_recorder = TaskRecorder(task=str(input), trace_id=trace_id)

        if AgentsUtils.get_current_trace():
            run_result = await Runner.run(self.agent, input, **kwargs)
        else:
            trace_id = trace_id or AgentsUtils.gen_trace_id()
            with trace(workflow_name="llm_agent", trace_id=trace_id):
                run_result = await Runner.run(self.agent, input, **kwargs)
        task_recorder.add_run_result(run_result)
        task_recorder.set_final_output(run_result.final_output)
        return task_recorder

    def run_streamed(
        self,
        input: str | list[TResponseInputItem],
        trace_id: str | None = None,
        **kwargs,
    ) -> RunResultStreaming:
        """以流式方式运行代理，适用于分块或增量输出场景。

        Args:
            input: 要发送给模型的输入，支持与 `run` 相同的输入类型。
            trace_id: 可选的链路跟踪 ID；若未提供将自动生成并用于 trace 上下文。

        Returns:
            RunResultStreaming: 流式运行的结果迭代/生成器对象，由底层 Runner 提供。
        """
        if AgentsUtils.get_current_trace():
            return Runner.run_streamed(self.agent, input, **kwargs)

        trace_id = trace_id or AgentsUtils.gen_trace_id()
        with trace(workflow_name="llm_agent", trace_id=trace_id):
            return Runner.run_streamed(self.agent, input, **kwargs)
