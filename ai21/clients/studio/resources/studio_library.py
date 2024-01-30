from typing import Optional, List

from ai21.ai21_http_client import AI21HTTPClient
from ai21.models import Mode, AnswerLength
from ai21.models.responses.file_response import FileResponse
from ai21.models.responses.library_answer_response import LibraryAnswerResponse
from ai21.models.responses.library_search_response import LibrarySearchResponse
from ai21.clients.studio.resources.studio_resource import StudioResource


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
        path: Optional[str] = None,
        labels: Optional[List[str]] = None,
        public_url: Optional[str] = None,
        **kwargs,
    ) -> str:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        files = {"file": open(file_path, "rb")}
        body = {"path": path, "labels": labels, "publicUrl": public_url}

        raw_response = self._post(url=url, files=files, body=body)

        return raw_response["fileId"]

    def get(self, file_id: str) -> FileResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}/{file_id}"
        raw_response = self._get(url=url)

        return FileResponse.from_dict(raw_response)

    def list(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs,
    ) -> List[FileResponse]:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        params = {"offset": offset, "limit": limit}
        raw_response = self._get(url=url, params=params)

        return [FileResponse.from_dict(file) for file in raw_response]

    def update(
        self,
        file_id: str,
        *,
        public_url: Optional[str] = None,
        labels: Optional[List[str]] = None,
        **kwargs,
    ) -> None:
        url = f"{self._client.get_base_url()}/{self._module_name}/{file_id}"
        body = {
            "publicUrl": public_url,
            "labels": labels,
        }
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
        path: Optional[str] = None,
        field_ids: Optional[List[str]] = None,
        max_segments: Optional[int] = None,
        **kwargs,
    ) -> LibrarySearchResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = {
            "query": query,
            "path": path,
            "fieldIds": field_ids,
            "maxSegments": max_segments,
        }
        raw_response = self._post(url=url, body=body)
        return LibrarySearchResponse.from_dict(raw_response)


class LibraryAnswer(StudioResource):
    _module_name = "library/answer"

    def create(
        self,
        question: str,
        *,
        path: Optional[str] = None,
        field_ids: Optional[List[str]] = None,
        labels: Optional[List[str]] = None,
        answer_length: Optional[AnswerLength] = None,
        mode: Optional[Mode] = None,
        **kwargs,
    ) -> LibraryAnswerResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = {
            "question": question,
            "path": path,
            "fieldIds": field_ids,
            "labels": labels,
            "answerLength": answer_length,
            "mode": mode,
        }
        raw_response = self._post(url=url, body=body)
        return LibraryAnswerResponse.from_dict(raw_response)
