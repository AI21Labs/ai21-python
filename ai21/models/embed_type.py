from enum import Enum


class EmbedType(str, Enum):
    QUERY = "query"
    SEGMENT = "segment"
