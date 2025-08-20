from dataclasses import dataclass
from typing import Dict, Any, Optional
from ..solana.client import SolanaClient
from ..solana.dex import DexRouter
from ..solana.wallet import TradingWallet

@dataclass
class TradeDecision:
    side: str  # "buy" | "sell" | "hold"
    mint_in: str
    mint_out: str
    amount_in: float
    reason: str

class StrategyEngine:
    def __init__(self, cfg: Dict[str, Any], solana: Optional[SolanaClient] = None):
        self.cfg = cfg
        self.solana = solana or SolanaClient()
        self.dex = DexRouter(self.solana)

    def signal(self) -> TradeDecision:
        # Placeholder signals turning into a buy
        base = self.cfg["universe"]["base_mint"]
        quote = self.cfg["universe"]["quote_mint"]
        amt = min(0.1, self.cfg["risk"]["max_sol_per_trade"])  # cap single trade
        return TradeDecision(side="buy", mint_in=base, mint_out=quote, amount_in=amt, reason="signal: breakout")

    def execute(self, decision: TradeDecision) -> Dict[str, Any]:
        if decision.side == "hold":
            return {"status": "noop", "reason": decision.reason}
        slip = int(self.cfg["risk"]["slippage_bps"])
        res = self.dex.swap(decision.mint_in, decision.mint_out, decision.amount_in, slippage_bps=slip)
        return {"status": "ok", "signature": res.signature, "tokens_out": res.tokens_out, "slippage_bps": res.slippage_bps}
