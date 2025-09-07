"""基础代理抽象定义模块。

该模块定义了代理应实现的最小接口 `BaseAgent`。
Docstring 使用 Google Python 风格，标题行（例如 Args, Returns, Raises）以英文保留，具体说明使用中文。
"""

import abc
from typing import Any

from .common import TaskRecorder


class BaseAgent:
    """代理基类，定义代理运行周期的最小契约。

    该类为代理实现提供三个主要异步方法：`run`（必须实现）、`build`（可选）和
    `cleanup`（可选）。具体代理应在子类中实现 `run` 方法以执行任务逻辑并返回
    `TaskRecorder` 实例来记录执行信息。
    """

    @abc.abstractmethod
    async def run(self, input: Any, trace_id: str | None = None, **kwargs) -> TaskRecorder:
        """执行代理的主入口，用于处理输入并返回任务记录器。

        Args:
            input: 要处理的输入数据，类型和语义由具体代理决定。
            trace_id: 可选的跟踪标识符，用于链路追踪与日志关联。
            **kwargs: 其他可选参数，会传递给具体实现以支持扩展。

        Returns:
            TaskRecorder: 描述执行过程、结果及相关元数据的记录对象。

        Raises:
            NotImplementedError: 如果子类没有实现该方法，则应抛出此异常。
        """
        raise NotImplementedError

    async def build(self):
        """可选的初始化钩子，在运行前进行必要的准备工作。

        例如加载模型、建立连接或准备缓存。默认实现为空，子类可按需重写。

        Returns:
            None: 默认不返回值。子类如需返回信息，可自行定义返回类型并在文档中说明。
        """
        pass

    async def cleanup(self):
        """可选的清理钩子，在运行后释放资源。

        例如关闭网络连接、释放占用的外部资源或保存最终状态。默认实现为空，
        子类可按需重写以执行清理逻辑。

        Returns:
            None: 默认不返回值。
        """
        pass
