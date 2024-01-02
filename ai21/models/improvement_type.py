from enum import Enum


class ImprovementType(str, Enum):
    FLUENCY = "fluency"
    VOCABULARY_SPECIFICITY = "vocabulary/specificity"
    VOCABULARY_VARIETY = "vocabulary/variety"
    CLARITY_SHORT_SENTENCES = "clarity/short-sentences"
    CLARITY_CONCISENESS = "clarity/conciseness"
