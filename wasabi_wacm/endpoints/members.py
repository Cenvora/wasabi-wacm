"""Mixin containing WACM member endpoints."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from requests import Response

from ._base import EndpointMixin


class MemberEndpoints(EndpointMixin):
    """Operations for `/v1/members` resources."""

    def create_member(self, payload: Mapping[str, Any]) -> Response:
        """POST /v1/members"""

        return self._request("POST", "/v1/members", json=payload)

    def get_members(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        id_: Optional[str | int] = None,
        status: Optional[str] = None,
        username: Optional[str] = None,
        sub_account_id: Optional[str | int] = None,
    ) -> Response:
        """GET /v1/members"""

        params = {
            "page": page,
            "size": size,
            "id": id_,
            "status": status,
            "username": username,
            "subAccountId": sub_account_id,
        }
        return self._request("GET", "/v1/members", params=params)

    def get_member(self, member_id: str | int) -> Response:
        """GET /v1/members/:id"""

        path = f"/v1/members/{member_id}"
        return self._request("GET", path)

    def update_member(self, member_id: str | int, payload: Mapping[str, Any]) -> Response:
        """PUT /v1/members/:id"""

        path = f"/v1/members/{member_id}"
        return self._request("PUT", path, json=payload)

    def delete_member(self, member_id: str | int) -> Response:
        """DELETE /v1/members/:id"""

        path = f"/v1/members/{member_id}"
        return self._request("DELETE", path)


__all__ = ["MemberEndpoints"]
