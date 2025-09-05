我将并行列出 utu 下前五个子目录（agents, config, context, db, env）的内容，以获取二级文件/子目录，用于构建树状视图（期望得到各子目录下的主要文件和子包）。 进度更新：已获取 utu 下前五个子目录的内容。接下来我将并行列出剩余子目录（eval、meta、models、patch、prompts）以完成树状结构，然后最后一批列出 `tool_maker、tools、tracing、ui、utils`。每次并行调用会说明目的与预期结果。 进度更新：已读取 `eval、meta、models、patch、prompts` 五个子目录。接下来并行读取最后一批 `tool_maker、tools、tracing、ui、utils` 以完成 utu 的全部二级目录列表。 任务收悉：我将继续并完成 utu 目录的树结构分析，并把二级目录及其重要文件/子包整理成树状备注。下面给出完整的 utu 目录树状结构与简短注释；若需要我可以继续展开任一子目录到更多层级并检查关键实现文件。

要求清单
- 列出 utu 目录下的全部子目录与主要文件（Done）
- 为每个子目录提供树状备注与简短说明（Done）

完整 utu 目录树状备注
📁 utu/
  __init__.py
  📁 agents/  
    __init__.py
    base_agent.py              — agent 基类与通用接口
    common.py                  — agent 通用辅助函数
    llm_agent.py               — 基于大模型的 agent 实现
    simple_agent.py            — 简化 agent 实现
    orchestra/                 — 协同/编排相关子包
    orchestra_agent.py         — orchestra 风格的 agent
  📁 config/
    __init__.py
    agent_config.py            — agent 配置定义
    base_config.py             — 基础配置类
    eval_config.py             — 评估相关配置
    loader.py                  — 配置加载器
    model_config.py            — 模型相关配置
  📁 context/
    __init__.py
    base_context_manager.py    — 上下文管理基类
    env_context_manager.py     — 环境上下文管理
  📁 db/
    __init__.py
    eval_datapoint.py          — 评估数据点模型
    tool_cache_model.py        — 工具缓存模型
    tracing_model.py           — 跟踪/追踪模型
    utu_basemodel.py           — db 基础模型定义（SQLModel/ORM）
  📁 env/
    __init__.py
    base_env.py                — 环境抽象基类
    browser_env.py             — 浏览器自动化环境实现
    shell_local_env.py         — 本地 shell 环境
    utils/                     — 环境工具集合
  📁 eval/
    __init__.py
    benchmarks/                — 基准/评测用例集合
    common.py
    data/                      — 评测数据
    processer/                 — 评测处理器
    utils.py
  📁 meta/
    __init__.py
    simple_agent_generator.py  — 生成简单 agent 的工具
  📁 models/
    react.py                   — 可能实现 React 风格模型交互
    react_converter.py
  📁 patch/
    runner.py                  — 补丁/热更新相关运行器
  📁 prompts/
    runner.py                  — prompts 运行/接口
    eval/                      — 评估相关 prompts
    meta/                      — 元 prompt
    tools/                     — 与工具交互的 prompts
  📁 tool_maker/
    __init__.py
    base.py                    — 构建工具的基类/框架
  📁 tools/
    __init__.py
    arxiv_toolkit.py
    audio_toolkit.py
    base.py
    bash_remote_tool.py
    bash_toolkit.py
    codesnip_toolkit.py
    document_toolkit.py
    documents/                 — 文档相关子模块
    file_edit_toolkit.py
    github_toolkit.py
    image_toolkit.py
    memory_toolkit.py
    python_executor_toolkit.py
    search/                    — 搜索工具集合
    search_toolkit.py
    serper_toolkit.py
    tabular_data_toolkit.py
    thinking_toolkit.py
    tione.py
    user_interaction_toolkit.py
    utils.py
    video_toolkit.py
    wikipedia_toolkit.py
  📁 tracing/
    __init__.py
    db_tracer.py
    notel_agents_instrumentor.py
    notel_agents_processor.py
    phoenix_utils.py
    setup.py
    toolcall_stat.py
  📁 ui/
    common.py
    dummy_chatbot.py
    frontend/
    gradio_chatbot.py
    webui_chatbot.py
  📁 utils/
    __init__.py
    agents_utils.py
    common.py
    env.py
    log.py
    openai_utils/
    path.py
    print_utils.py
    sqlmodel_utils.py
    token.py
    tool_cache.py