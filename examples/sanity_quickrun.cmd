@echo off
REM === Quick Run Sanity for [REDACTED]-ALPHA ===
REM Creates venv (if missing), installs deps, and runs the agent once.

REM 1) Ensure Python 3.11 is available as 'py -3.11'
py -3.11 --version >NUL 2>&1
IF ERRORLEVEL 1 (
  echo [ERROR] Python 3.11 not found. Install Python 3.11 and retry.
  exit /b 1
)

REM 2) Create venv if missing
IF NOT EXIST .venv\Scripts\python.exe (
  echo [+] Creating virtualenv...
  py -3.11 -m venv .venv
)

REM 3) Activate venv (cmd.exe)
call .venv\Scripts\activate.bat

REM 4) Install minimal deps
python -m pip install --upgrade pip
pip install -r requirements.txt

REM 5) OPTIONAL: Set secrets/RPC (uncomment & fill if you want to see pubkey vary)
REM set AGENT1_SK_B58=...
REM set SOLANA_RPC_URL=https://api.mainnet-beta.solana.com
REM set SOLANA_WS_URL=wss://api.mainnet-beta.solana.com

REM 6) Run ALPHA once; prints JSON (pubkey, decision, fake signature, etc.)
python -m src.agents.agent.runner run src/agents/agent/configs/agent_redacted_1.yaml

REM 7) Deactivate venv
deactivate
