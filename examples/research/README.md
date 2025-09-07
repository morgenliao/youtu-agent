# 深度研究示例

此示例通过编排三个专门的 `SimpleAgent` 实例来实现“计划和执行”工作流。它受到 `openai-agents` 库中的 [research_bot 示例](https://github.com/openai/openai-agents-python/tree/main/examples/research_bot) 的启发，并展示了多代理协作的轻量级方法。

## 工作流

该过程是一个简单而强大的管道：

1.  **计划**：`PlannerAgent` 接收用户的查询并生成 `WebSearchPlan`（搜索术语列表）。它使用 Pydantic 模型来实现可靠的结构化输出。

2.  **搜索**：`SearchAgent` 接收计划并使用 `asyncio` 和 `SearchToolkit` **并行** 执行所有网络搜索。它为每个结果返回简洁的摘要。

3.  **撰写**：`WriterAgent` 将所有搜索摘要合成到一个最终的详细报告中，也使用 Pydantic `ReportData` 模型定义。

此示例突显了如何链接代理、在它们之间传递结构化数据，并使用并行性提高效率，提供了一个轻量级的替代方案来替代正式的 `OrchestraAgent`。

