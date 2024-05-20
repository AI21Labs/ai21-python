from __future__ import annotations
from typing import Optional, List


from ai21.ai21_http_client import AI21HTTPClient
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import FileResponse, LibraryAnswerResponse, LibrarySearchResponse
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given


class StudioLibrary(StudioResource):
    _module_name = "library/files"

    def __init__(self, client: AI21HTTPClient):
        super().__init__(client)
        self.files = LibraryFiles(client)
        self.search = LibrarySearch(client)
        self.answer = LibraryAnswer(client)


class LibraryFiles(StudioResource):
    _module_name = "library/files"

    def create(
        self,
        file_path: str,
        *,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        public_url: Optional[str] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> str:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        files = {"file": open(file_path, "rb")}
        body = remove_not_given({"path": path, "labels": labels, "publicUrl": public_url, **kwargs})

        raw_response = self._post(url=url, files=files, body=body, response_cls=dict)

        return raw_response["fileId"]

    def get(self, file_id: str) -> FileResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}/{file_id}"

        return self._get(url=url, response_cls=FileResponse)

    def list(
        self,
        *,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> List[FileResponse]:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        params = remove_not_given({"offset": offset, "limit": limit})

        return self._get(url=url, params=params, response_cls=List[FileResponse])

    def update(
        self,
        file_id: str,
        *,
        public_url: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> None:
        url = f"{self._client.get_base_url()}/{self._module_name}/{file_id}"
        body = remove_not_given(
            {
                "publicUrl": public_url,
                "labels": labels,
                **kwargs,
            }
        )
        self._put(url=url, body=body)

    def delete(self, file_id: str) -> None:
        url = f"{self._client.get_base_url()}/{self._module_name}/{file_id}"
        self._delete(url=url)


class LibrarySearch(StudioResource):
    _module_name = "library/search"

    def create(
        self,
        query: str,
        *,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        field_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        max_segments: Optional[int] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> LibrarySearchResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = remove_not_given(
            {
                "query": query,
                "path": path,
                "fieldIds": field_ids,
                "maxSegments": max_segments,
                **kwargs,
            }
        )

        return self._post(url=url, body=body, response_cls=LibrarySearchResponse)


class LibraryAnswer(StudioResource):
    _module_name = "library/answer"

    def create(
        self,
        question: str,
        *,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        field_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> LibraryAnswerResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = remove_not_given(
            {
                "question": question,
                "path": path,
                "fieldIds": field_ids,
                "labels": labels,
                **kwargs,
            }
        )

        return self._post(url=url, body=body, response_cls=LibraryAnswerResponse)
