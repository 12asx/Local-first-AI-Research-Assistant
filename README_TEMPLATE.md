# ResearchAgent

> Local-first AI research assistant for scientific paper reading, retrieval, conversation memory, and citation management.

ResearchAgent is an early-stage, local-first research assistant with optional cloud model integrations. It combines PDF/DOCX parsing, local literature search, optional online academic retrieval, citation links, and persistent conversations. It is **not yet** a fully autonomous LangGraph agent; its core functionality is literature retrieval and assisted reading.

> **Status: research prototype.** Results and citations must be checked against the original papers. Please do not host the current local API publicly without authentication and security hardening.

## Features

- Local PDF/DOCX collection and searchable index
- Literature reading and comparison with source page references when available
- Configurable OpenAI-compatible LLM endpoint; optional DeepSeek document parsing
- Independent online search settings
- Persistent local chat history, user-confirmed long-term notes, and citation bookmarks
- Windows desktop shortcut launcher; local browser interface

## Quick start (Windows)

1. Install Python 3.11 or 3.12 and Git.
2. Clone the repository: `git clone https://github.com/YOUR_USERNAME/ResearchAgent.git`
3. Enter the project: `cd ResearchAgent`
4. Install dependencies: `python -m pip install -r requirements.txt`
5. Double-click `启动 ResearchAgent.vbs` (or use `start_windows_debug.bat` to diagnose errors).
6. Open `http://127.0.0.1:8765/workspace` (the port may differ if it is occupied).

> Confirm file names and launch steps against the exact version you publish before claiming they work on a clean computer. Do not upload your real API keys or PDF collection.

## Configuration

Use the application settings page to configure a compatible LLM endpoint and separate online search. Most features can run locally; using a cloud model or a provider's document API may transmit selected data to that provider and may incur usage charges. See the application's privacy notices.

## Data privacy

User PDFs, citation databases, conversation histories, cached results, settings containing credentials, and local logs are excluded from this public repository. Runtime files are stored locally in `data/` and the user's chosen paper directory.

## Architecture

Python backend + browser workspace + local document retrieval + optional model/search providers. Add an actual architecture diagram here after auditing the source tree.

## Tests

```bash
python -m pytest -q
```

## Limitations

- PDF text extraction can fail on scans and multi-column layouts.
- Model answers are not verified scientific measurements.
- Local endpoints are not production authentication or multitenant services.
- Platform support outside Windows may require additional setup.

## Contributing

See `CONTRIBUTING.md`. Issues and pull requests are welcome.

## License

**To be determined after reviewing the source-code ownership and third-party dependency licenses, especially PyMuPDF's AGPL/commercial terms.** Add a reviewed `LICENSE` file before declaring the repository open source.
