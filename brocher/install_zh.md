# 🚀 Youtu-Agent 部署指南（中文）

本指南帮助你快速部署和运行 Youtu-Agent 智能体框架。

---

## 环境准备

1. 克隆仓库并安装依赖：

> [!NOTE]
> 本项目使用 **Python 3.12+**。推荐使用 [uv](https://github.com/astral-sh/uv) 进行依赖管理。

```bash
git clone https://github.com/TencentCloudADP/youtu-agent.git
cd youtu-agent
uv sync
source ./.venv/bin/activate
cp .env.example .env  # 你需要配置相关环境变量!
```

> [!NOTE]
> 请配置 `.env` 文件中的相关环境变量，例如 LLM API keys。

---

## 快速开始

Youtu-Agent 内置了配置文件。例如，默认配置文件 (`configs/agents/default.yaml`) 定义了一个带有搜索工具的简单 Agent：

```bash
# 启动交互式 CLI 聊天机器人（需配置 SERPER_API_KEY 和 JINA_API_KEY）
python scripts/cli_chat.py --stream --config default
# 如果不使用搜索工具，可运行：
python scripts/cli_chat.py --stream --config base
```

更多内容请参考：[快速开始文档](https://tencentcloudadp.github.io/youtu-agent/quickstart)

---

## 示例探索

本仓库提供了多个可直接运行的示例。例如，自动生成 SVG 信息图：

```bash
python examples/svg_generator/main_web.py
```

> [!NOTE]
> 要使用 WebUI，请安装 `utu_agent_ui` 包。参考 [文档](https://tencentcloudadp.github.io/youtu-agent/frontend/#installation)。

更多示例请参考：[示例文档](https://tencentcloudadp.github.io/youtu-agent/examples)

---

## 运行评测

Youtu-agent 支持在标准数据集上进行基准测试。例如，在 WebWalkerQA 上运行评测：

```bash
# 数据集预处理
python scripts/data/process_web_walker_qa.py

# 运行评测（需配置评测相关环境变量）
python scripts/run_eval.py --config_name ww --exp_id <your_exp_id> --dataset WebWalkerQA_15 --concurrency 5
```

结果会保存到本地，并可在分析平台中进一步查看。详见 [评测分析](./frontend/exp_analysis/README.md)。

更多内容请参考：[评测文档](https://tencentcloudadp.github.io/youtu-agent/eval)

---

如需更多高级部署方式（如 Docker），请参考仓库中的 `docker/README.md`。
