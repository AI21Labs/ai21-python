from typing import Dict
from typing_extensions import TypedDict, Required


class DocumentSchema(TypedDict, total=False):
    content: Required[str]
    id: str
    metadata: Dict[str, str]
