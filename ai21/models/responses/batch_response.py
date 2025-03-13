from typing import Literal

from ai21.models.ai21_base_model import AI21BaseModel


class RequestCounts(AI21BaseModel):
    total: int
    completed: int
    failed: int


class Batch(AI21BaseModel):
    id: str
    """The ID of the batch."""
    status: Literal["FAILED", "PROCESSING", "COMPLETED", "EXPIRED", "CANCELLED", "PENDING"]

    """The current status of the batch."""
    endpoint: str
    """The AI21 API endpoint used by the batch."""

    created_at: int
    """The Unix timestamp (in seconds) for when the batch was created."""

    completed_at: int | None = None
    """The Unix timestamp (in seconds) for when the batch was completed."""

    cancelled_at: int | None = None
    """The Unix timestamp (in seconds) for when the batch was cancelled."""

    expires_at: int
    """The Unix timestamp (in seconds) for when the batch will expire."""

    expired_at: int | None = None
    """The Unix timestamp (in seconds) for when the batch expired."""

    request_counts: RequestCounts
    """The request counts for different statuses within the batch."""

    metadata: dict

    output_file: str | None = None
    """The path to the file containing the outputs of successfully executed requests."""

    error_file: str | None = None
    """The path to the file containing the outputs of requests with errors."""

    total_input_tokens: int
    """The total number of input tokens in the batch."""
