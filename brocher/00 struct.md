
进度说明：我已读取仓库根目录和各主要一级目录的内容，下面按目录给出树状备注；若需更深入展开某个子目录（列出更多层级或文件详情），告诉我要展开的目录即可。

## 顶层重要目录（概览）
根目录包含的主要一级目录/文件（只列出主要目录与重要文件）：
- 配置/元数据与文档：CHANGELOG.md、CONTRIBUTING.md、LICENSE、Makefile、mkdocs.yml、pyproject.toml、README_ZH.md
- 主要目录：brocher、configs、demo、docker、examples、frontend、scripts、tests、utu
- 虚拟环境或隐藏：.venv、.git、.github 等

## 逐个一级目录树状备注

### brocher
- `README.md` — 该目录总体说明
- `install_zh.md` — 安装文档（中文）
- `docs/`
  - 文档集（示例）：`agents.md`、`config.md`、`docker.md`、`env.md`、`eval.md`、`examples.md`、`frontend.md`、`index.md`、`quickstart.md`、`quickstart_beginner.md`、`tools.md`
  - 资源文件夹：`assets/`、`examples_output/`、`ref/`、`stylesheets/`

备注：docs 存放用户/部署/使用文档，是项目文档中心。

---

### configs
- 子目录/文件（配置集合）
  - `agents/`
  - `eval/`
  - examples
  - `exp/`
  - `model/`
  - `simple_agents/`
  - `tools/`
  - 主要 yaml：`base.yaml`、`default.yaml`、`orchestra.yaml`

备注：存放运行时与不同 agent/工具的配置模板与样例。

---

### demo
- `demo.py` — CLI 或脚本 demo
- `demo_web.py` — Web demo（可能基于 Gradio/Flask）
- `dummy_client.py` — 测试/示例客户端脚本

备注：用于快速体验项目功能的示例入口。

---

### docker
- `.env.docker.example` — Docker 环境变量示例
- `Dockerfile` — 容器构建脚本
- `README.md` — Docker 使用说明

备注：包含容器化相关配置与说明。

---

### examples
- 子目录（多个示例项目/功能集）：
  - `data_analysis/` — 数据分析示例
  - `file_manager/` — 文件管理示例
  - `gui_agent_datamaker/`
  - `mcp/`
  - `paper_collector/` 论文
  - `research/`        研究
  - `svg_generator/`   svg生成器
  - `wide_research/`   广域研究

备注：每个子目录通常包含可运行示例和 README，便于学习不同功能模块。

---

### frontend
- `exp_analysis/` — 当前列出的子目录
- （仓库也包含前端相关配置文件/项目文件，参见主仓库树用于前端构建）

备注：前端相关资源/实验分析界面，若需展开可进一步列出 `exp_analysis` 内容及可能存在的 `package.json`、`src/` 等。

---

### scripts
- 文件与子目录：
  - `cli_chat.py`                    智能体脚手架
  - `gen_simple_agent.py`            生成简单的智能体
  - `run_eval.py`                    执行评估
  - `run_eval_judge.py`              执行评估分析
  - `analysis/` — 分析脚本集合（例如 `tool_usage.py` 在子目录内）
  - `data/` — 数据处理脚本
  - `db/` — 数据库相关脚本（例如 `dump_db.py`、`clear_cache.py` 在仓库其他位置）
  - `tracing/` — 跟踪/调试脚本
  - `utils/` — 实用脚本合集

备注：存放各类可执行脚本与工具，是运维与实验常用位置。

---

### 📁 tests  
- 结构示例：
  - `agents/`
  - `conftest.py`
  - `env/`
  - `eval/`
  - `models/`
  - `test_config.py`
  - `tools/`
  - `tracing/`
  - `utils/`

备注：测试套件，含单元/集成测试及测试辅助文件。

---

### 📁 utu
- 包根文件：`__init__.py`
- 主要子包/模块：
  - `agents/`
  - `config/`
  - `context/`
  - `db/`
  - `env/`
  - `eval/`
  - `meta/`
  - `models/`
  - `patch/`
  - `prompts/`
  - `tool_maker/`
  - `tools/`
  - `tracing/`
  - `ui/`
  - `utils/`

备注：这是项目的核心 Python 包，包含业务逻辑、agent 实现、模型接口、工具与上下文管理。若要定位主要代码实现，优先查看 agents、models、tools。
