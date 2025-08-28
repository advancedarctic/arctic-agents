@echo off
REM Example local runs
REM Set secret keys via env (base58-encoded)
REM set AGENT1_SK_B58=...
REM set AGENT2_SK_B58=...
REM set AGENT3_SK_B58=...

REM Optional: override RPCs
REM set SOLANA_RPC_URL=https://api.mainnet-beta.solana.com
REM set SOLANA_WS_URL=wss://api.mainnet-beta.solana.com

REM ALPHA
python -m src.agents.agent.runner run src/agents/agent/configs/agent_redacted_1.yaml
REM BETA
python -m src.agents.agent.runner run src/agents/agent/configs/agent_redacted_2.yaml
REM GAMMA
python -m src.agents.agent.runner run src/agents/agent/configs/agent_redacted_3.yaml
