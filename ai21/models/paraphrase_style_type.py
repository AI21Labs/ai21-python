from enum import Enum


class ParaphraseStyleType(str, Enum):
    LONG = "long"
    SHORT = "short"
    FORMAL = "formal"
    CASUAL = "casual"
    GENERAL = "general"
