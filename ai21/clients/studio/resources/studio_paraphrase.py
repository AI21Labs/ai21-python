from typing import Optional

from ai21.clients.common.paraphrase_base import Paraphrase
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import ParaphraseStyleType, ParaphraseResponse


class StudioParaphrase(StudioResource, Paraphrase):
    def create(
        self,
        text: str,
        *,
        style: Optional[ParaphraseStyleType] = None,
        start_index: Optional[int] = None,
        end_index: Optional[int] = None,
        **kwargs,
    ) -> ParaphraseResponse:
        body = self._create_body(
            text=text,
            style=style,
            start_index=start_index,
            end_index=end_index,
            **kwargs,
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=ParaphraseResponse)


class AsyncStudioParaphrase(AsyncStudioResource, Paraphrase):
    async def create(
        self,
        text: str,
        *,
        style: Optional[ParaphraseStyleType] = None,
        start_index: Optional[int] = None,
        end_index: Optional[int] = None,
        **kwargs,
    ) -> ParaphraseResponse:
        body = self._create_body(
            text=text,
            style=style,
            start_index=start_index,
            end_index=end_index,
            **kwargs,
        )

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=ParaphraseResponse)
