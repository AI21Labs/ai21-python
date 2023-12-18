from typing import Optional


class APIError(Exception):
    def __init__(self, status_code: int, details: Optional[str] = None):
        super().__init__(details)
        self.details = details
        self.status_code = status_code

    def __str__(self) -> str:
        return f"Failed with http status code: {self.status_code} ({type(self).__name__}). Details: {self.details}"


class BadRequest(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(400, details)


class Unauthorized(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(401, details)


class AccessDenied(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(403, details)


class NotFound(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(404, details)


class APITimeoutError(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(408, details)


class UnprocessableEntity(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(422, details)


class TooManyRequests(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(429, details)


class ServerError(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(500, details)


class ServiceUnavailable(APIError):
    def __init__(self, details: Optional[str] = None):
        super().__init__(500, details)


class AI21ClientException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.message}"


class MissingInputException(AI21ClientException):
    def __init__(self, field_name: str, call_name: str):
        message = f"{field_name} is required for the {call_name} call"
        super().__init__(message)


class UnsupportedInputException(AI21ClientException):
    def __init__(self, field_name: str, call_name: str):
        message = f"{field_name} is unsupported for the {call_name} call"
        super().__init__(message)


class UnsupportedDestinationException(AI21ClientException):
    def __init__(self, destination_name: str, call_name: str):
        message = f'Destination of type {destination_name} is unsupported for the "{call_name}" call'
        super().__init__(message)


class OnlyOneInputException(AI21ClientException):
    def __init__(self, field_name1: str, field_name2: str, call_name: str):
        message = f"{field_name1} or {field_name2} is required for the {call_name} call, but not both"
        super().__init__(message)


class WrongInputTypeException(AI21ClientException):
    def __init__(self, key: str, expected_type: type, given_type: type):
        message = f"Supplied {key} should be {expected_type}, but {given_type} was passed instead"
        super().__init__(message)


class EmptyMandatoryListException(AI21ClientException):
    def __init__(self, key: str):
        message = f"Supplied {key} is empty. At least one element should be present in the list"
        super().__init__(message)


class MissingApiKeyException(AI21ClientException):
    def __init__(self):
        message = "API key must be supplied either globally in the ai21 namespace, or to be provided in the call args"
        super().__init__(message)
        self.message = message


class NoSpecifiedRegionException(AI21ClientException):
    def __init__(self):
        message = "No AWS region provided"
        super().__init__(message)
        self.message = message


class ModelPackageDoesntExistException(AI21ClientException):
    def __init__(self, model_name: str, region: str, version: Optional[str] = None):
        message = f"model_name: {model_name} doesn't exist in region: {region}"

        if version is not None:
            message += f" with version: {version}"

        super().__init__(message)
        self.message = message
