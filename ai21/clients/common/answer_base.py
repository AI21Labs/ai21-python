from abc import ABC, abstractmethod
from typing import Any, Dict

from ai21.models import AnswerResponse


class Answer(ABC):
    _module_name = "answer"

    @abstractmethod
    def create(
        self,
        context: str,
        question: str,
        **kwargs,
    ) -> AnswerResponse:
        """

        :param context: A string containing the document context for which the question will be answered
        :param question: A string containing the question to be answered based on the provided context.
        :param kwargs:
        :return:
        """
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> AnswerResponse:
        return AnswerResponse.from_dict(json)

    def _create_body(
        self,
        context: str,
        question: str,
        **kwargs,
    ) -> Dict[str, Any]:
        return {"context": context, "question": question, **kwargs}
