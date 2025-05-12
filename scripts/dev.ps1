param([string]$Task = "help")

function Setup {
  py -3.11 -m venv .venv
  .\.venv\Scripts\Activate.ps1
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  Write-Host "Env ready. Activate with: .\.venv\Scripts\Activate.ps1"
}

function Lint { ruff check .; black --check .; mypy src }
function Fix  { ruff check --select I --fix .; black . }
function Test { pytest -q }
function Agent { python -m src.agents.agent.baseline_agent }

switch ($Task) {
  "setup" { Setup }
  "lint"  { Lint }
  "fix"   { Fix }
  "test"  { Test }
  "agent" { Agent }
  default {
    Write-Host "Usage: powershell -File scripts/dev.ps1 <task>"
    Write-Host "Tasks: setup | lint | fix | test | agent"
  }
}
