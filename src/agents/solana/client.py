from typing import Optional
from solana.rpc.api import Client
from solana.rpc.websocket_api import connect as ws_connect
from .settings import SolanaSettings

class SolanaClient:
    def __init__(self, settings: Optional[SolanaSettings] = None):
        self.settings = settings or SolanaSettings()
        self.http = Client(self.settings.rpc_url, commitment=self.settings.default_commitment)

    def get_slot(self) -> int:
        return self.http.get_slot()["result"]

    async def ws_slots(self):
        # Example: stream slots over WS
        async with ws_connect(self.settings.ws_url) as websocket:
            sub = await websocket.slot_subscribe()
            try:
                async for msg in websocket:
                    yield msg
            finally:
                await websocket.slot_unsubscribe(sub)
