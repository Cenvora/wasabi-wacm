"""Core HTTP plumbing shared by the WACM client mixins."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, MutableMapping, Optional

import requests
from requests import Response
from requests.auth import AuthBase, HTTPBasicAuth
from requests.exceptions import HTTPError

from .exceptions import WACMRequestError


def _clean_params(params: Mapping[str, Any] | None) -> MutableMapping[str, Any] | None:
    if not params:
        return None
    cleaned: dict[str, Any] = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, bool):
            cleaned[key] = str(value).lower()
        else:
            cleaned[key] = value
    return cleaned or None


@dataclass
class BaseWACMClient:
    """Shared HTTP configuration and helpers for endpoint mixins."""

    base_url: str = "https://api.wacm.wasabisys.com/api"
    username: Optional[str] = None
    password: Optional[str] = None
    timeout: Optional[float | tuple[float, float]] = 30
    session: Optional[requests.Session] = None
    auth: Optional[AuthBase] = None

    def __post_init__(self) -> None:
        self.base_url = self.base_url.rstrip("/")
        if self.auth is None and self.username and self.password:
            self.auth = HTTPBasicAuth(self.username, self.password)
        if self.session is None:
            self.session = requests.Session()
        self.session.headers.setdefault("Accept", "application/json")

    # Context manager helpers -------------------------------------------------
    def close(self) -> None:
        if self.session is not None:
            self.session.close()

    def __enter__(self) -> "BaseWACMClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        self.close()

    # Internal request helper -------------------------------------------------
    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
    ) -> Response:
        if self.session is None:
            raise RuntimeError("Client session not initialised")
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=_clean_params(params),
                json=json,
                auth=self.auth,
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response
        except HTTPError as exc:  # pragma: no cover - thin wrapper
            response = exc.response
            status_code = response.status_code if response is not None else "unknown"
            message = f"WACM request failed: {method} {url} -> {status_code}"
            if response is not None and response.text:
                message = f"{message}: {response.text}"
            raise WACMRequestError(message, response) from exc


__all__ = ["BaseWACMClient"]
