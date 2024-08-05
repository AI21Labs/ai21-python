from abc import ABC, abstractmethod
from typing import Optional, Any, Dict, cast

from ai21.models import ParaphraseStyleType, ParaphraseResponse
from ai21.models._pydantic_compatibility import _from_dict


class Paraphrase(ABC):
    _module_name = "paraphrase"

    @abstractmethod
    def create(
        self,
        text: str,
        *,
        style: Optional[ParaphraseStyleType] = None,
        start_index: Optional[int] = 0,
        end_index: Optional[int] = None,
        **kwargs,
    ) -> ParaphraseResponse:
        """

        :param text: The input text to be paraphrased.
        :param style: Controls length and tone
        :param start_index: Specifies the starting position of the paraphrasing process in the given text
        :param end_index: specifies the position of the last character to be paraphrased, including the character
         following it. If the parameter is not provided, the default value is set to the length of the given text.
        :param kwargs:
        :return:
        """
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> ParaphraseResponse:
        return cast(_from_dict(obj=ParaphraseResponse, obj_dict=json), ParaphraseResponse)

    def _create_body(
        self,
        text: str,
        style: Optional[str],
        start_index: Optional[int],
        end_index: Optional[int],
        **kwargs,
    ) -> Dict[str, Any]:
        return {
            "text": text,
            "style": style,
            "startIndex": start_index,
            "endIndex": end_index,
            **kwargs,
        }
