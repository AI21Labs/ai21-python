from typing import Dict, Any

import pytest

from ai21.models import Penalty
from ai21.models._pydantic_compatibility import _to_dict, _from_dict
from ai21.models.ai21_base_model import IS_PYDANTIC_V2, AI21BaseModel
from tests.unittests.models.response_mocks import (
    get_answer_response__answer_in_context_not_none,
    get_answer_response__answer_in_context_is_none,
    get_chat_response,
    get_chat_completions_response,
    get_completions_response,
    get_gec_response,
    get_paraphrase_response,
    get_segmentation_response,
    get_summarize_response,
    get_summarize_by_segment_response,
)


def test_penalty__to_dict__when_has_none_fields__should_filter_them_out():
    penalty = Penalty(scale=0.5, apply_to_whitespaces=True)
    assert penalty.to_dict() == {"scale": 0.5, "applyToWhitespaces": True}


def test_penalty__to_json__when_has_none_fields__should_filter_them_out():
    penalty = Penalty(scale=0.5, apply_to_whitespaces=True)
    if IS_PYDANTIC_V2:
        assert penalty.to_json() == '{"scale":0.5,"applyToWhitespaces":true}'
    else:
        assert penalty.to_json() == '{"scale": 0.5, "applyToWhitespaces": true}'


def test_penalty__from_dict__should_return_instance_with_given_values():
    penalty = Penalty.from_dict({"scale": 0.5, "applyToWhitespaces": True})
    assert penalty.scale == 0.5
    assert penalty.apply_to_whitespaces is True
    assert penalty.apply_to_emojis is None


def test_penalty__from_json__should_return_instance_with_given_values():
    penalty = Penalty.from_json('{"scale":0.5,"applyToWhitespaces":true}')
    assert penalty.scale == 0.5
    assert penalty.apply_to_whitespaces is True
    assert penalty.apply_to_emojis is None


@pytest.mark.parametrize(
    ids=[
        "answer_response__answer_in_context",
        "answer_response__answer_not_in_context",
        "chat_response",
        "chat_completions_response",
        "completion_response",
        "gec_response",
        "paraphrase_response",
        "segmentation_response",
        "summarization_response",
        "summarize_by_segment_response",
    ],
    argnames=[
        "response_obj",
        "expected_dict",
        "response_cls",
    ],
    argvalues=[
        (get_answer_response__answer_in_context_not_none()),
        (get_answer_response__answer_in_context_is_none()),
        (get_chat_response()),
        (get_chat_completions_response()),
        (get_completions_response()),
        (get_gec_response()),
        (get_paraphrase_response()),
        (get_segmentation_response()),
        (get_summarize_response()),
        (get_summarize_by_segment_response()),
    ],
)
def test_to_dict__should_serialize_to_dict__(
    response_obj: AI21BaseModel, expected_dict: Dict[str, Any], response_cls: Any
):
    assert response_obj.to_dict() == expected_dict
    assert _to_dict(model_object=response_obj, by_alias=True) == expected_dict


@pytest.mark.parametrize(
    ids=[
        "answer_response__answer_in_context_not_none",
        "answer_response__answer_in_context_is_none",
        "chat_response",
        "chat_completions_response",
        "completion_response",
        "gec_response",
        "paraphrase_response",
        "segmentation_response",
        "summarization_response",
        "summarize_by_segment_response",
    ],
    argnames=[
        "response_obj",
        "expected_dict",
        "response_cls",
    ],
    argvalues=[
        (get_answer_response__answer_in_context_not_none()),
        (get_answer_response__answer_in_context_is_none()),
        (get_chat_response()),
        (get_chat_completions_response()),
        (get_completions_response()),
        (get_gec_response()),
        (get_paraphrase_response()),
        (get_segmentation_response()),
        (get_summarize_response()),
        (get_summarize_by_segment_response()),
    ],
)
def test_from_dict__should_serialize_from_dict__(
    response_obj: AI21BaseModel,
    expected_dict: Dict[str, Any],
    response_cls: Any,
):
    assert response_cls.from_dict(expected_dict) == response_obj
    assert _from_dict(obj=response_obj, obj_dict=expected_dict) == response_obj
