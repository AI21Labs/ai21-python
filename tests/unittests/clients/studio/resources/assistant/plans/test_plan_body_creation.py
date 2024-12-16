from typing import Callable, List, Dict, Any, Type, Union

from pydantic import BaseModel
from ai21.clients.common.beta.assistant.plans import BasePlans
from ai21.errors import CodeParsingError
from ai21.models.responses.plan_response import PlanResponse, ListPlanResponse
from ai21.types import NotGiven, NOT_GIVEN
import pytest


class PlanTestClass(BasePlans):
    def create(
        self,
        *,
        assistant_id: str,
        code: Union[str, Callable],
        schemas: Union[List[Dict[str, Any]], List[Type[BaseModel]], NotGiven] = NOT_GIVEN,
        **kwargs,
    ) -> PlanResponse:
        pass

    def list(self, *, assistant_id: str) -> ListPlanResponse:
        pass

    def retrieve(self, *, assistant_id: str, plan_id: str) -> PlanResponse:
        pass

    def modify(
        self, *, assistant_id: str, plan_id: str, code: str, schemas: Union[List[Dict[str, Any]], NotGiven] = NOT_GIVEN
    ) -> PlanResponse:
        pass


def test_create_body__when_pass_code_str__should_return_dict():
    # Arrange
    code = "code"

    # Act
    result = PlanTestClass()._create_body(code=code)

    # Assert
    assert result == {"code": code}


def test_create_body__when_pass_code_callable__should_return_dict():
    # Arrange
    def code():
        return "code"

    # Act
    result = PlanTestClass()._create_body(code=code)

    # Assert
    assert result == {"code": 'def code():\n        return "code"'}


def test_create_body__when_pass_code_and_dict_schemas__should_return_dict_with_schemas():
    # Arrange
    code = "code"
    schemas = [{"type": "object", "properties": {"name": {"type": "string"}}}]

    # Act
    result = PlanTestClass()._create_body(code=code, schemas=schemas)

    # Assert
    assert result == {"code": code, "schemas": schemas}


class TestSchema(BaseModel):
    name: str
    age: int


def test_create_body__when_pass_code_and_pydantic_schemas__should_return_dict_with_converted_schemas():
    # Arrange
    code = "code"
    schemas = [TestSchema]

    # Act
    result = PlanTestClass()._create_body(code=code, schemas=schemas)

    # Assert
    expected_schema = {
        "properties": {"age": {"title": "Age", "type": "integer"}, "name": {"title": "Name", "type": "string"}},
        "required": ["name", "age"],
        "title": "TestSchema",
        "type": "object",
    }
    assert result == {"code": code, "schemas": [expected_schema]}


def test_create_body__when_pass_code_and_not_given_schemas__should_return_dict_without_schemas():
    # Arrange
    code = "code"

    # Act
    result = PlanTestClass()._create_body(code=code, schemas=NOT_GIVEN)

    # Assert
    assert result == {"code": code}


def test_create_body__when_pass_empty_schemas_list__should_return_dict_with_empty_schemas():
    # Arrange
    code = "code"
    schemas = []

    # Act
    result = PlanTestClass()._create_body(code=code, schemas=schemas)

    # Assert
    assert result == {"code": code, "schemas": schemas}


def test_create_body__when_cannot_get_source_code__should_raise_code_parsing_error():
    # Arrange
    class CallableWithoutSource:
        def __call__(self):
            return "result"

        # Override __code__ to simulate a built-in function or method
        @property
        def __code__(self):
            raise AttributeError("'CallableWithoutSource' object has no attribute '__code__'")

    code = CallableWithoutSource()

    # Act & Assert
    with pytest.raises(CodeParsingError):
        PlanTestClass()._create_body(code=code)
