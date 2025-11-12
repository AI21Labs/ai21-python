from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class UploadMode(str, Enum):
    BATCH = "batch"


class BatchStatusCount(BaseModel):
    status: str
    count: int


class BatchStatusResponse(BaseModel):
    batch_id: str = Field(description="The UUID of the batch")
    total_documents: int = Field(description="Total number of documents in the batch")
    statuses: List[BatchStatusCount] = Field(description="List of document counts by status")
