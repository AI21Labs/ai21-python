from enum import Enum


class SummaryMethod(str, Enum):
    SEGMENTS = "segments"
    GUIDED = "guided"
    FULL_DOCUMENT = "fullDocument"
