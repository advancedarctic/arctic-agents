# ai-agents-baseline (Windows-first, bones only)

Minimal skeleton for building **LLM agents** and **future training**.
No training/downloads by default.

## Quickstart (PowerShell)
```powershell
powershell -File scripts/dev.ps1 setup
Copy-Item .env.example .env   # add keys later if needed
powershell -File scripts/dev.ps1 agent
