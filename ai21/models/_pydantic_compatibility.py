from __future__ import annotations

from typing import Dict, Any

from pydantic import VERSION, BaseModel

IS_PYDANTIC_V2 = VERSION.startswith("2.")


def _to_dict(model_object: BaseModel, **kwargs) -> Dict[str, Any]:
    if IS_PYDANTIC_V2:
        return model_object.model_dump(**kwargs)

    return model_object.dict(**kwargs)


def _to_json(model_object: BaseModel, **kwargs) -> str:
    if IS_PYDANTIC_V2:
        return model_object.model_dump_json(**kwargs)

    return model_object.json(**kwargs)


def _from_dict(obj: "AI21BaseModel", obj_dict: Any, **kwargs) -> BaseModel:  # noqa: F821
    if IS_PYDANTIC_V2:
        return obj.model_validate(obj_dict, **kwargs)

    return obj.parse_obj(obj_dict, **kwargs)


def _from_json(obj: "AI21BaseModel", json_str: str, **kwargs) -> BaseModel:  # noqa: F821
    if IS_PYDANTIC_V2:
        return obj.model_validate_json(json_str, **kwargs)

    return obj.parse_raw(json_str, **kwargs)
