from typing import Optional
from solders.keypair import Keypair
from base58 import b58decode

class TradingWallet:
    def __init__(self, secret_key_b58: Optional[str] = None):
        if secret_key_b58:
            sk = b58decode(secret_key_b58)
            self.kp = Keypair.from_bytes(sk)
        else:
            self.kp = Keypair()
    @property
    def pubkey(self) -> str:
        return str(self.kp.pubkey())
