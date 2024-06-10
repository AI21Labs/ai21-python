from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.errors import EmptyMandatoryListError
from ai21.models import ImprovementType, ImprovementsResponse


class Improvements(ABC):
    _module_name = "improvements"

    @abstractmethod
    def create(self, text: str, types: List[ImprovementType], **kwargs) -> ImprovementsResponse:
        """

        :param text: The input text to be improved.
        :param types: Types of improvements to apply.
        :param kwargs:
        :return:
        """
        pass

    def _create_body(self, text: str, types: List[str], **kwargs) -> Dict[str, Any]:
        return {"text": text, "types": types, **kwargs}

    def _validate_types(self, types: List[ImprovementType]):
        if len(types) == 0:
            raise EmptyMandatoryListError("types")
