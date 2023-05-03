import json
from channels.generic.websocket import AsyncWebsocketConsumer
import dotenv
import os
from pathlib import Path

from ChatGPT.settings import BASE_DIR

# Build paths inside the project like this: BASE_DIR / 'subdir'.
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = None

    async def connect(self):
        await self.accept()

    # Receive message from WebSocket

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        self.message = text_data_json['message']
        response = await self.chat_with_gpt()

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            response,
        }))

    async def chat_message(self, event):
        response = await self.chat_with_gpt()

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            response,
        }))

    async def chat_with_gpt(self):
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.message}
            ]
        )
        return response.choices[0].message['content']
