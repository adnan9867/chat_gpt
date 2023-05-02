import dotenv
import os

from ChatGPT.settings import BASE_DIR

# Build paths inside the project like this: BASE_DIR / 'subdir'.
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


class JWTAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers'])
        if b'authorization' in headers:
            try:
                token = headers[b'authorization'].decode()
                if not token == os.environ["TOKEN"]:
                    raise Exception("Not authenticated")
                return await self.app(scope, receive, send)
            except Exception as e:
                pass
        raise Exception("Not authenticated")
