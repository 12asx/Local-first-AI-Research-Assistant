[Uploading README.md…]()
# ResearchAgent

**Local-first AI Research Assistant · 本地优先的 AI 科研助手**

[简体中文](#简体中文) | [English](#english)

> **Project status / 项目状态:** Public beta / 开源测试版  
> **Platform / 平台:** Windows-first, browser-based / 优先支持 Windows，浏览器界面  
> **Scope / 定位:** Literature retrieval and AI-assisted research workflows, **not yet a fully autonomous LangGraph agent**.  
> 文献检索与大模型辅助科研工作流，**目前并非具备自主规划与工具循环能力的完整 LangGraph Agent**。

ResearchAgent is a local-first research workspace for managing papers, reading scientific literature, chatting with configurable AI models, and retrieving saved discussions with traceable sources.

ResearchAgent 是一个以本地数据管理为基础的科研工作台，整合文献管理、论文阅读、模型问答、历史内容召回和可追溯引用。

---

## 简体中文

### ✨ 项目简介

ResearchAgent 希望把科研阅读过程中分散的步骤整合到一个界面：导入论文、检索资料、分析文章、保存研究背景，以及在后续对话中找回先前的讨论内容。它面向材料、物理、化学、生物等不同研究领域，不预设特定材料体系或研究方向。

目前项目以 **Python 后端 + 本地 Web 界面 + 文献检索增强问答（RAG）** 为主要架构。使用者可更换大模型服务；联网检索与模型问答分别配置。

### 🧩 主要功能

| 模块 | 功能 |
| --- | --- |
| 本地文献库 | 导入可提取文本的 PDF / DOCX，建立本地检索索引；支持配置文献文件夹 |
| 论文阅读 | 单篇论文讲解、关键章节提取、两篇论文比较；在可用时提供原 PDF 页码来源 |
| AI 科研问答 | 通过兼容 OpenAI Chat Completions 的接口连接不同模型服务 |
| 联网检索 | 独立配置网络搜索服务；网络能力不依赖固定聊天模型 |
| 长期记忆 | 将研究背景、偏好和重要结论保存为可编辑、可置顶的本地笔记 |
| 历史内容召回 | 保存聊天问答记录，并根据旧问题或旧回答内容搜索、回顾之前的讨论 |
| 引用收藏 | 保存论文标题、DOI、摘录、页码及个人备注，回到相关原文或原会话核对 |
| 图片问答 | 上传图片参与对话；发送前可以移除单张图片或清空待发送附件 |
| 桌面启动 | Windows 快捷启动器；应用在本机运行，通过浏览器访问 |

> **提示：** 模型生成的科研结论、参考文献、数值与页码必须与原始论文核对。历史回答的恢复不代表历史答案已经得到科学验证。

### 🚀 快速开始（Windows）

**环境要求**

- Windows 10/11；推荐 Python 3.11 或 3.12。
- 首次安装依赖需要互联网连接；使用云端模型、在线检索也需要相应的网络和服务凭据。
- 如果只使用本地文献管理和历史检索，部分功能不需要 API Key。

**1. 下载代码**

在 GitHub 仓库点击 **Code → Download ZIP** 并解压，或者执行：

```bash
git clone https://github.com/YOUR_USERNAME/ResearchAgent.git
cd ResearchAgent
```

将 `YOUR_USERNAME` 替换成实际的 GitHub 用户名。

**2. 安装 Python 依赖**

在项目根目录打开 PowerShell：

```powershell
python -m pip install -r requirements.txt
```

建议在 Python 虚拟环境中安装依赖，以免影响其他科研软件。

**3. 启动应用**

- 双击 `启动 ResearchAgent.vbs`，由启动器启动本地服务并打开浏览器。
- 也可以使用 `start_windows.bat`；如遇故障，尝试项目中提供的调试启动脚本（如果当前发行版包含）。
- 通常可通过 `http://127.0.0.1:8765/workspace` 打开工作台。**如果该端口被占用，以启动器实际打开的地址为准。**
- 使用结束后，通过 `关闭 ResearchAgent.vbs` 关闭后台服务；只关闭浏览器标签页不一定会停止服务。

如发行包中包含 `安装桌面快捷方式.vbs`，可运行一次创建桌面和开始菜单入口。移动程序文件夹后，需要重新安装快捷方式。

### ⚙️ 模型与联网配置

在网页界面顶部进入 **模型设置**，配置 API Base URL、模型 ID 和 API Key。请填写所用服务商当前实际支持的模型 ID。

**模型设置与联网检索相互独立：** 开启“联网”开关并不代表一定能搜索成功，还需要配置并测试可用的搜索服务。在线检索失败时，程序应展示失败状态，而不是把模型已有知识伪装成实时检索结果。

项目提供可选的 DeepSeek 文档解析流程。在用户明确确认之后，原始 PDF 可能上传至服务商，并产生文档解析和模型 Token 费用。不同模型和接口的能力、费用与支持情况，请以服务商官方说明为准。

### 📚 基本使用流程

1. 在 **文献库** 中导入论文，或切换到现有文献目录并建立索引。
2. 在 **科研对话** 中提出问题；需要联网时开启对应选项。
3. 讲解论文时，优先通过来源链接回到原 PDF 核查关键结果、图表和测试条件。
4. 对需要长期保留的研究背景、偏好或结论，在 **长期记忆** 中明确保存。
5. 通过 **历史** 标签检索过去的提问及回答，或打开原会话继续讨论。
6. 将常用论文与摘录保存到 **引用夹**，定期导出备份。

### 🔐 数据与隐私

ResearchAgent 默认面向**单人本机使用**。应用通常仅监听 `127.0.0.1`，当前项目不应在没有身份认证、权限控制及安全加固的情况下直接部署到公网。

本地运行数据可能包含：

```text
data/                  # 历史会话、记忆、数据库、索引、缓存等
papers/                # 默认本地文献目录（如使用）
.env                   # 可能包含服务凭据；绝不可提交
```

这些私人资料**不应上传到公共 GitHub 仓库**。公开之前请检查 `.gitignore`、已暂存文件及 Git 历史，移除 API Key、私人论文、个人路径和测试日志。

调用云端模型或文档解析接口时，选定的对话内容、长期记忆片段、论文摘录或经确认的 PDF 可能发送给服务商。请勿将尚未公开或受保密限制的研究材料发送给未经授权的服务。

### 🛠️ 开发与测试

```bash
python -m pytest -q
```

预期项目结构（以实际发布的源码为准）：

```text
ResearchAgent/
├── research_demo/             # Python 后端
├── static/                    # Web 前端
├── assets/                    # 图标与静态资源
├── tests/                     # 自动化测试
├── docs/                      # 使用文档
├── requirements.txt
├── 启动 ResearchAgent.vbs
├── 关闭 ResearchAgent.vbs
├── README.md
└── .gitignore
```

### ⚠️ 已知限制

- 扫描版 PDF、复杂双栏排版和图表读取仍可能不完整；纯文本抽取不等于完整视觉理解。
- 自动生成的页码与引用可能不准确，正式写作时需要核验。
- 历史内容召回只覆盖当前本地数据目录中**确实保存过**的聊天，不会自动获取其他应用中的历史。
- 多轮历史归纳可能消耗模型 Token；全文解析通常也需要额外资源。
- 当前版本主要是科研 RAG 工作台，并非具备自主实验规划和工具执行闭环的完整自治 Agent。
- Windows 为主要测试平台；其他平台可能需要调整启动方式。

### 🗺️ 后续计划

- 提升复杂 PDF、公式与图表的抽取及跨页阅读能力。
- 改进历史语义检索、长期记忆筛选与来源可解释性。
- 增加可配置的多步骤科研 Agent 工作流与工具调用。
- 完善跨平台部署、错误监控和可复现性测试。

### 🤝 贡献与反馈

欢迎提交 Issues 和 Pull Requests。建议在提交问题时提供复现步骤、预期行为和运行环境。**请勿上传真实 API Key、私人聊天、未公开论文或含敏感信息的日志。**

### 📄 许可证

**许可证待确定。** 请先核实源代码、第三方依赖与资源的权属及许可义务（特别是 PDF 解析依赖），再添加正式 `LICENSE` 文件。**在许可证明确之前，公开可见不等于他人已获得自由使用和再分发的许可。**

---

## English

### ✨ Overview

ResearchAgent is a **local-first AI research workspace** designed to bring everyday literature workflows into one interface: organize papers, retrieve relevant sources, read and compare articles, chat with configurable language models, save research context, and recover previous discussions.

The project is intended for researchers across disciplines, including physics, materials science, chemistry, and biology. It does not assume a particular material system or research topic.

The current architecture centers on a **Python backend, a local browser interface, and retrieval-augmented generation (RAG)**. LLM providers and web search providers are configurable separately.

### 🧩 Features

| Module | Capabilities |
| --- | --- |
| Local library | Import text-extractable PDF and DOCX files, build a searchable local index, and select a literature folder |
| Paper reading | Explain individual papers, retrieve relevant sections, and compare two papers with page references when available |
| AI research chat | Connect to configurable OpenAI Chat Completions-compatible model endpoints |
| Web search | Configure online search independently of the selected chat model |
| Long-term notes | Save, edit, and pin research background, preferences, and important conclusions |
| Conversation recall | Persist question–answer history; find previous discussions by questions and saved answer content |
| Citation bookmarks | Save bibliographic details, excerpts, page references, and research notes |
| Image attachments | Upload images for chat, remove individual pending attachments, or clear the queue before sending |
| Desktop launcher | Launch a local browser workspace through Windows shortcuts |

> **Research integrity:** AI-generated interpretations, measurements, citations, and page numbers must be checked against the original publications. Recalling an old answer does not validate its scientific accuracy.

### 🚀 Quick Start (Windows)

**Requirements**

- Windows 10/11; Python 3.11 or 3.12 recommended.
- Internet access for first-time dependency installation and optional cloud services.
- An API key is only necessary for features that call an external provider. Local library management and some history functions can work without one.

**1. Download the project**

Use **Code → Download ZIP** on GitHub, or clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ResearchAgent.git
cd ResearchAgent
```

Replace `YOUR_USERNAME` with the repository owner's GitHub username.

**2. Install dependencies**

```powershell
python -m pip install -r requirements.txt
```

A dedicated Python virtual environment is recommended.

**3. Launch**

- Double-click `启动 ResearchAgent.vbs` to start the local service and open the browser.
- Alternatively, use `start_windows.bat`. Consult the debug launcher if included in your release.
- The workspace is usually available at `http://127.0.0.1:8765/workspace`. If the port is occupied, use the URL opened by the launcher.
- To stop the service, run `关闭 ResearchAgent.vbs`; closing the browser tab alone may not stop the backend.

If `安装桌面快捷方式.vbs` is included, run it once to add desktop and Start menu shortcuts. Reinstall the shortcut after moving the project folder.

### ⚙️ Model and Search Configuration

Open **Model Settings** in the web interface to enter your provider's API Base URL, supported model ID, and API key.

**Web search is separate from model inference.** Enabling the search toggle does not guarantee live retrieval unless a working search provider has been configured and tested. The application should report search failures instead of presenting model knowledge as verified live results.

An optional DeepSeek document-parsing workflow may upload a PDF to the provider **only after explicit user confirmation**. File parsing and model usage can incur charges. Availability, models, and pricing depend on the provider.

### 📚 Typical Workflow

1. Import PDF/DOCX papers into the **Library** or select an existing paper folder.
2. Ask questions in **Research Chat**, optionally enabling web search.
3. Follow source links to check claims, figures, methods, and measurement conditions in the original PDFs.
4. Save durable research preferences or conclusions in **Long-term Memory**.
5. Search earlier questions and answers in **History**, then open the original conversation.
6. Bookmark important sources in the **Citation Shelf** and export backups periodically.

### 🔐 Data Privacy and Security

ResearchAgent is designed primarily for **single-user local operation**. The server normally binds to `127.0.0.1`. **Do not expose the current API to the public internet without authentication, access controls, and security hardening.**

Private runtime data may include:

```text
data/                  # Conversations, memory, databases, indexes, caches
papers/                # Default local paper folder (if used)
.env                   # Potential credentials; never commit
```

**Do not include private data in a public GitHub repository.** Review `.gitignore`, staged files, and Git history for credentials, copyrighted PDFs, personal file paths, private conversations, and logs.

When using a cloud LLM or document-processing provider, selected prompts, memory excerpts, retrieved paper passages, or explicitly uploaded PDFs may be transmitted to that provider. Do not send confidential or unpublished materials without authorization.

### 🛠️ Development and Testing

Run the test suite:

```bash
python -m pytest -q
```

Illustrative project structure (verify against the release being published):

```text
ResearchAgent/
├── research_demo/             # Python backend
├── static/                    # Web interface
├── assets/                    # Icons and assets
├── tests/                     # Automated tests
├── docs/                      # Documentation
├── requirements.txt
├── 启动 ResearchAgent.vbs
├── 关闭 ResearchAgent.vbs
├── README.md
└── .gitignore
```

### ⚠️ Known Limitations

- Scanned PDFs, complex multi-column layouts, and visual figures may not be parsed completely. Text extraction is not the same as full visual understanding.
- Generated citations and page numbers can be incorrect and must be verified before publication.
- Conversation recall only covers chat records actually saved in the current local data directory; it cannot automatically recover chats from unrelated apps.
- Summarizing history and processing entire documents may incur additional token or parsing costs.
- The project is currently a research-oriented RAG workspace, **not** a fully autonomous experimental or LangGraph agent.
- Windows is the primary target; other operating systems may need a different launcher.

### 🗺️ Roadmap

- Improve extraction of complex papers, equations, figures, and cross-page content.
- Improve semantic history retrieval, long-term memory selection, and source transparency.
- Introduce configurable multistep research-agent workflows and tool orchestration.
- Expand cross-platform support, diagnostics, and reproducibility tests.

### 🤝 Contributing

Issues and pull requests are welcome. When reporting bugs, include clear reproduction steps, expected behavior, and your environment. **Never attach real API keys, private chat histories, unpublished papers, or sensitive logs.**

### 📄 License

**License pending.** Review source ownership, third-party dependencies (especially PDF-processing libraries), and asset permissions before adding a definitive `LICENSE`. **A publicly visible repository does not automatically grant unrestricted reuse or redistribution rights.**

---

**ResearchAgent · Read critically, preserve context, and trace every source.**  
**ResearchAgent · 认真阅读，保留上下文，让每条结论都有迹可循。**
