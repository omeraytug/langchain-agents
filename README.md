# LangChain Agents

LangChain-based agents using Ollama. Run from the project root with uv.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- Ollama (with base URL and bearer token for your Llama setup)

## Setup

1. Clone the repo and go to the project root.

2. Install dependencies and lockfile (creates/updates `uv.lock`):

   ```bash
   uv sync
   ```

   To only refresh the lockfile without installing:

   ```bash
   uv lock
   ```

3. Copy the example env file and add your values:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and set `OLLAMA_BASE_URL` and `OLLAMA_BEARER_TOKEN`.

## Agents

| Agent | Description |
|-------|-------------|
| **research_agent** | Fetches a URL, summarizes the page and answers questions about it. Replies in Swedish. |
| **lang_agent** | Fixes grammar/spelling in any language and translates text to a language you specify. |
| **summarize_agent** | Summarizes text you paste; can output bullets or keywords. Keeps the same language as the input. |

## Run

From the project root (no need to activate a venv; uv runs inside its own env):

```bash
uv run research_agent.py
uv run lang_agent.py
uv run summarize_agent.py
```
