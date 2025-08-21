# Bank Statement Parser Agent

This project builds an **autonomous coding agent** that generates custom parsers for bank statement PDFs.

## Features
- ✅ Agent loop: Plan → Generate Parser → Run Tests → Fix (max 3 attempts)
- ✅ Uses **LangGraph** for autonomy
- ✅ CLI: `python agent.py --target icici`
- ✅ Extensible to new banks (just change target)
- ✅ Parsers return `pandas.DataFrame` matching CSV schema
- ✅ Tests with pytest
- ✅ Logging shows retries & autonomy

## Quickstart
```bash
git clone <your-fork-url>
cd karbon-agent-coder
pip install -r requirements.txt
python agent.py --target icici
pytest
