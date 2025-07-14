from channels.generic.websocket import AsyncWebsocketConsumer
import json
from main.hints import get_hints

class HintsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        hints = await get_hints(data)
        await self.send(text_data=json.dumps({'hints': hints}))

    async def disconnect(self, close_code):
        pass
