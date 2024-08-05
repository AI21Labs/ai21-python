from typing import Optional


class AI21APIError(Exception):
    def __init__(self, status_code: int, details: Optional[str] = None):
        super().__init__(details)
        self.details = details
        self.status_code = status_code

    def __str__(self) -> str:
        return f"Failed with http status code: {self.status_code} ({type(self).__name__}). Details: {self.details}"


class BadRequest(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(400, details)


class Unauthorized(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(401, details)


class AccessDenied(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(403, details)


class NotFound(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(404, details)


class APITimeoutError(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(408, details)


class UnprocessableEntity(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(422, details)


class ModelErrorException(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(424, details)


class TooManyRequestsError(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(429, details)


class AI21ServerError(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(500, details)


class ServiceUnavailable(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(500, details)


class AI21Error(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.message}"


class MissingApiKeyError(AI21Error):
    def __init__(self):
        message = "API key must be supplied either globally in the ai21 namespace, or to be provided in the call args"
        super().__init__(message)
        self.message = message


class ModelPackageDoesntExistError(AI21Error):
    def __init__(self, model_name: str, region: str, version: Optional[str] = None):
        message = f"model_name: {model_name} doesn't exist in region: {region}"

        if version is not None:
            message += f" with version: {version}"

        super().__init__(message)
        self.message = message


class EmptyMandatoryListError(AI21Error):
    def __init__(self, key: str):
        message = f"Supplied {key} is empty. At least one element should be present in the list"
        super().__init__(message)


class StreamingDecodeError(AI21Error):
    def __init__(self, chunk: str, error_message: Optional[str] = None):
        message = f"Failed to decode chunk: {chunk} in stream. Please check the stream format."
        if error_message:
            message = f"{message} Error: {error_message}"
        super().__init__(message)


class InternalDependencyException(AI21APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(530, details)
