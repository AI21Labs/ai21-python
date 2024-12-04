from ai21.clients.studio.resources.beta.assistant.assistant import AsyncAssistant
from ai21.clients.studio.resources.beta.assistant.thread import AsyncThread
from ai21.clients.studio.resources.studio_conversational_rag import AsyncStudioConversationalRag
from ai21.clients.studio.resources.studio_resource import AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient


class AsyncBeta(AsyncStudioResource):
    def __init__(self, client: AsyncAI21HTTPClient):
        super().__init__(client)

        self.assistants = AsyncAssistant(client)
        self.conversational_rag = AsyncStudioConversationalRag(client)
        self.threads = AsyncThread(client)
