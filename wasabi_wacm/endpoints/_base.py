"""Shared typing contract for endpoint mixins."""

from __future__ import annotations

from typing import Any, Mapping

from requests import Response


class EndpointMixin:
    """Declares the request helper supplied by BaseWACMClient."""

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
    ) -> Response:
        raise NotImplementedError


__all__ = ["EndpointMixin"]
