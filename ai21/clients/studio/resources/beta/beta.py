from ai21.clients.studio.resources.batch.batches import Batches
from ai21.clients.studio.resources.maestro.maestro import Maestro
from ai21.clients.studio.resources.studio_conversational_rag import (
    StudioConversationalRag,
)
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.http_client.http_client import AI21HTTPClient


class Beta(StudioResource):
    def __init__(self, client: AI21HTTPClient):
        super().__init__(client)

        self.conversational_rag = StudioConversationalRag(client)
        self.maestro = Maestro(client)
        self.batches = Batches(client)
