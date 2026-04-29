"""Exception types for the WACM client package."""

from typing import Optional

from requests import Response


class WACMRequestError(RuntimeError):
    """Wraps HTTP errors raised while talking to the WACM API."""

    def __init__(self, message: str, response: Optional[Response]) -> None:
        super().__init__(message)
        self.response = response


__all__ = ["WACMRequestError"]
