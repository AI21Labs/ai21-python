from abc import ABC
from typing import Optional, Any, Dict

from ai21.resources.responses.answer_response import AnswerResponse


class Answer(ABC):
    _module_name = "answer"

    def create(
        self,
        context: str,
        question: str,
        *,
        answer_length: Optional[str] = None,
        mode: Optional[str] = None,
        **kwargs,
    ) -> AnswerResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> AnswerResponse:
        return AnswerResponse.from_dict(json)

    def _create_body(
        self,
        context: str,
        question: str,
        answer_length: Optional[str],
        mode: Optional[str],
    ) -> Dict[str, Any]:
        return {"context": context, "question": question, "answerLength": answer_length, "mode": mode}
