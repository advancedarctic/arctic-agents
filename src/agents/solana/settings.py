from pydantic_settings import BaseSettings
from pydantic import Field

class SolanaSettings(BaseSettings):
    rpc_url: str = Field(default="https://api.mainnet-beta.solana.com")
    ws_url: str = Field(default="wss://api.mainnet-beta.solana.com")
    default_commitment: str = Field(default="confirmed")
    jito_tip_lamports: int = Field(default=0)  # set >0 to use Jito tip bundles

    class Config:
        env_prefix = "SOLANA_"  # e.g., SOLANA_RPC_URL
