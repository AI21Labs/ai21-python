from ai21.clients.studio.resources.batch.async_batches import AsyncBatches
from ai21.clients.studio.resources.maestro.maestro import AsyncMaestro
from ai21.clients.studio.resources.studio_conversational_rag import (
    AsyncStudioConversationalRag,
)
from ai21.clients.studio.resources.studio_resource import AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient


class AsyncBeta(AsyncStudioResource):
    def __init__(self, client: AsyncAI21HTTPClient):
        super().__init__(client)

        self.conversational_rag = AsyncStudioConversationalRag(client)
        self.maestro = AsyncMaestro(client)
        self.batches = AsyncBatches(client)
