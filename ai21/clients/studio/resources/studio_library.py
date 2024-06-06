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
        files = {"file": open(file_path, "rb")}
        body = remove_not_given({"path": path, "labels": labels, "publicUrl": public_url, **kwargs})

        raw_response = self._post(path=f"/{self._module_name}", files=files, body=body, response_cls=dict)

        return raw_response["fileId"]

    def get(self, file_id: str) -> FileResponse:
        return self._get(path=f"/{self._module_name}/{file_id}", response_cls=FileResponse)

    def list(
        self,
        *,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> List[FileResponse]:
        params = remove_not_given({"offset": offset, "limit": limit})

        return self._get(path=f"/{self._module_name}", params=params, response_cls=List[FileResponse])

    def update(
        self,
        file_id: str,
        *,
        public_url: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> None:
        body = remove_not_given(
            {
                "publicUrl": public_url,
                "labels": labels,
                **kwargs,
            }
        )
        self._put(path=f"/{self._module_name}/{file_id}", body=body)

    def delete(self, file_id: str) -> None:
        self._delete(path=f"/{self._module_name}/{file_id}")


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
        body = remove_not_given(
            {
                "query": query,
                "path": path,
                "fieldIds": field_ids,
                "maxSegments": max_segments,
                **kwargs,
            }
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=LibrarySearchResponse)


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
        body = remove_not_given(
            {
                "question": question,
                "path": path,
                "fieldIds": field_ids,
                "labels": labels,
                **kwargs,
            }
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=LibraryAnswerResponse)
