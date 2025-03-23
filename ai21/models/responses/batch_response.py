from typing import Literal, Optional

from ai21.models.ai21_base_model import AI21BaseModel


class RequestCounts(AI21BaseModel):
    total: int
    completed: int
    failed: int


class Batch(AI21BaseModel):
    id: str
    """The ID of the batch."""
    status: Literal["FAILED", "PROCESSING", "COMPLETED", "EXPIRED", "CANCELLED", "PENDING", "STALE"]

    """The current status of the batch."""
    endpoint: str
    """The AI21 API endpoint used by the batch."""

    created_at: int
    """The Unix timestamp (in seconds) for when the batch was created."""

    completed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the batch was completed."""

    cancelled_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the batch was cancelled."""

    request_counts: RequestCounts
    """The request counts for different statuses within the batch."""

    metadata: Optional[dict] = None

    output_file: Optional[str] = None
    """The path to the file containing the outputs of successfully executed requests."""

    error_file: Optional[str] = None
    """The path to the file containing the outputs of requests with errors."""
