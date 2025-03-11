from ai21.clients.common.maestro.maestro import BaseMaestro
from ai21.clients.studio.resources.maestro.run import MaestroRun, AsyncMaestroRun
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient


class Maestro(StudioResource, BaseMaestro):
    def __init__(self, client: AI21HTTPClient):
        super().__init__(client)

        self.runs = MaestroRun(client)


class AsyncMaestro(AsyncStudioResource, BaseMaestro):
    def __init__(self, client: AsyncAI21HTTPClient):
        super().__init__(client)

        self.runs = AsyncMaestroRun(client)
