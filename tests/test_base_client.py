from __future__ import annotations

from typing import Any

import pytest
import requests
from requests.auth import HTTPBasicAuth

from wasabi_wacm.base import BaseWACMClient, _clean_params
from wasabi_wacm.exceptions import WACMRequestError


class FakeSession:
    def __init__(self, response: requests.Response | None = None) -> None:
        self.headers: dict[str, str] = {}
        self.calls: list[dict[str, Any]] = []
        self.closed = False
        self.response = response if response is not None else make_response()

    def request(self, **kwargs: Any) -> requests.Response:
        self.calls.append(kwargs)
        return self.response

    def close(self) -> None:
        self.closed = True


def make_response(
    status_code: int = 200,
    body: str = '{"ok": true}',
    url: str = "https://example.test/api/v1/resource",
) -> requests.Response:
    response = requests.Response()
    response.status_code = status_code
    response._content = body.encode("utf-8")
    response.url = url
    response.reason = "OK" if status_code < 400 else "Bad Request"
    return response


def test_clean_params_omits_none_and_serializes_booleans() -> None:
    assert _clean_params(
        {
            "none": None,
            "enabled": True,
            "disabled": False,
            "name": "demo",
            "count": 3,
        }
    ) == {
        "enabled": "true",
        "disabled": "false",
        "name": "demo",
        "count": 3,
    }


def test_clean_params_returns_none_for_empty_results() -> None:
    assert _clean_params(None) is None
    assert _clean_params({}) is None
    assert _clean_params({"unused": None}) is None


def test_client_sets_default_session_headers_and_basic_auth() -> None:
    session = FakeSession()

    client = BaseWACMClient(
        username="user",
        password="secret",
        session=session,  # type: ignore[arg-type]
    )

    assert session.headers["Accept"] == "application/json"
    assert isinstance(client.auth, HTTPBasicAuth)


def test_client_does_not_override_existing_auth_or_accept_header() -> None:
    session = FakeSession()
    session.headers["Accept"] = "application/vnd.example+json"
    auth = HTTPBasicAuth("custom-user", "custom-secret")

    client = BaseWACMClient(
        username="user",
        password="secret",
        session=session,  # type: ignore[arg-type]
        auth=auth,
    )

    assert client.auth is auth
    assert session.headers["Accept"] == "application/vnd.example+json"


def test_context_manager_closes_session() -> None:
    session = FakeSession()

    with BaseWACMClient(session=session) as client:  # type: ignore[arg-type]
        assert client.session is session
        assert session.closed is False

    assert session.closed is True


def test_request_builds_url_cleans_params_and_returns_response() -> None:
    response = make_response()
    session = FakeSession(response)
    client = BaseWACMClient(
        base_url="https://example.test/api/",
        username="user",
        password="secret",
        timeout=(1, 5),
        session=session,  # type: ignore[arg-type]
    )

    result = client._request(
        "POST",
        "/v1/resource",
        params={
            "includeDeleted": False,
            "includeKeys": True,
            "ignored": None,
            "page": 2,
        },
        json={"name": "demo"},
    )

    assert result is response
    assert session.calls == [
        {
            "method": "POST",
            "url": "https://example.test/api/v1/resource",
            "params": {
                "includeDeleted": "false",
                "includeKeys": "true",
                "page": 2,
            },
            "json": {"name": "demo"},
            "auth": client.auth,
            "timeout": (1, 5),
        }
    ]


def test_request_wraps_http_errors_with_response_details() -> None:
    response = make_response(status_code=400, body='{"error": "bad request"}')
    session = FakeSession(response)
    client = BaseWACMClient(
        base_url="https://example.test/api",
        session=session,  # type: ignore[arg-type]
    )

    with pytest.raises(WACMRequestError) as exc_info:
        client._request("GET", "/v1/fail")

    assert exc_info.value.response is response
    assert "GET https://example.test/api/v1/fail -> 400" in str(exc_info.value)
    assert '{"error": "bad request"}' in str(exc_info.value)


def test_request_requires_initialized_session() -> None:
    client = BaseWACMClient()
    client.session = None

    with pytest.raises(RuntimeError, match="Client session not initialised"):
        client._request("GET", "/v1/resource")
