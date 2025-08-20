import os, json, typer, yaml
from pathlib import Path
from .strategy import StrategyEngine
from ..solana.wallet import TradingWallet
from ..solana.settings import SolanaSettings

app = typer.Typer(add_completion=False)

def load_cfg(cfg_path: str):
    with open(cfg_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@app.command()
def run(cfg: str = typer.Argument(..., help="Path to agent YAML config")):
    cfgd = load_cfg(cfg)
    wallet_env = cfgd.get("wallet_env_key")
    sk = os.getenv(wallet_env, "")
    wallet = TradingWallet(secret_key_b58=sk if sk else None)

    # Settings (optionally override via env)
    s = SolanaSettings()  # reads SOLANA_* env vars
    engine = StrategyEngine(cfgd)

    decision = engine.signal()
    result = engine.execute(decision)

    payload = {
        "agent": cfgd.get("name"),
        "wallet_pubkey": wallet.pubkey,
        "decision": decision.__dict__,
        "result": result,
    }
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    app()
