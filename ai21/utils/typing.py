from typing import Any, Dict, get_args, cast

from ai21.types import NotGiven


def is_not_given(value: Any) -> bool:
    return isinstance(value, NotGiven)


def remove_not_given(body: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in body.items() if not is_not_given(v)}


def to_camel_case(snake_str: str) -> str:
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


def to_lower_camel_case(snake_str: str) -> str:
    # We capitalize the first letter of each component except the first one
    # with the 'capitalize' method and join them together.
    camel_string = to_camel_case(snake_str)
    return snake_str[0].lower() + camel_string[1:]


def extract_type(type_to_extract: Any) -> type:
    args = get_args(type_to_extract)
    try:
        return cast(type, args[0])
    except IndexError as err:
        raise RuntimeError(
            f"Expected type {type_to_extract} to have a type argument at index 0 but it did not"
        ) from err
