"""Mixin containing WACM account endpoints."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from requests import Response

from ._base import EndpointMixin


class ChannelAccountEndpoints(EndpointMixin):
    """Operations for `/v1/channel-accounts` resources."""

    def create_channel_account(self, payload: Mapping[str, Any]) -> Response:
        """POST /v1/channel-accounts"""

        return self._request("POST", "/v1/channel-accounts", json=payload)

    def create_channel_account_user(self, payload: Mapping[str, Any]) -> Response:
        """POST /v1/channel-accounts/users"""

        return self._request("POST", "/v1/channel-accounts/users", json=payload)

    def get_channel_accounts(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        id_: Optional[str | int] = None,
        status: Optional[str] = None,
        name: Optional[str] = None,
        contact_email: Optional[str] = None,
        control_account_id: Optional[str | int] = None,
        include_deleted_sub_accounts: Optional[bool] = None,
    ) -> Response:
        """GET /v1/channel-accounts"""

        params = {
            "page": page,
            "size": size,
            "id": id_,
            "status": status,
            "name": name,
            "contactEmail": contact_email,
            "controlAccountId": control_account_id,
            "includeDeletedSubAccounts": include_deleted_sub_accounts,
        }
        return self._request("GET", "/v1/channel-accounts", params=params)

    def get_channel_account(
        self,
        channel_account_id: str | int,
        *,
        include_deleted_sub_accounts: Optional[bool] = None,
    ) -> Response:
        """GET /v1/channel-accounts/:channelAccountId"""

        params = {"includeDeletedSubAccounts": include_deleted_sub_accounts}
        path = f"/v1/channel-accounts/{channel_account_id}"
        return self._request("GET", path, params=params)

    def update_channel_account(
        self,
        channel_account_id: str | int,
        payload: Mapping[str, Any],
    ) -> Response:
        """PUT /v1/channel-accounts/:channelAccountId"""

        path = f"/v1/channel-accounts/{channel_account_id}"
        return self._request("PUT", path, json=payload)

    def delete_channel_account_user(self, user_id: str | int) -> Response:
        """DELETE /v1/channel-accounts/users/:userId"""

        path = f"/v1/channel-accounts/users/{user_id}"
        return self._request("DELETE", path)

    def delete_channel_account(self, account_id: str | int) -> Response:
        """DELETE /v1/channel-accounts/:id"""

        path = f"/v1/channel-accounts/{account_id}"
        return self._request("DELETE", path)


__all__ = ["ChannelAccountEndpoints"]
