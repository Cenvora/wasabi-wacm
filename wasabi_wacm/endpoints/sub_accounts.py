"""Mixin containing WACM sub-account endpoints."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from requests import Response

from ._base import EndpointMixin


class SubAccountEndpoints(EndpointMixin):
    """Operations for `/v1/sub-accounts` resources."""

    def create_sub_account(self, payload: Mapping[str, Any]) -> Response:
        """POST /v1/sub-accounts"""

        return self._request("POST", "/v1/sub-accounts", json=payload)

    def get_sub_account_bucket_utilization(
        self,
        sub_account_id: str | int,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        latest: Optional[bool] = None,
        name: Optional[str] = None,
        bucket_number: Optional[str | int] = None,
        region: Optional[str] = None,
    ) -> Response:
        """GET /v1/sub-accounts/:subAccountId/buckets"""

        params = {
            "page": page,
            "size": size,
            "from": from_,
            "to": to,
            "latest": latest,
            "name": name,
            "bucketNumber": bucket_number,
            "region": region,
        }
        path = f"/v1/sub-accounts/{sub_account_id}/buckets"
        return self._request("GET", path, params=params)

    def get_sub_accounts(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        id_: Optional[str | int] = None,
        name: Optional[str] = None,
        control_account_id: Optional[str | int] = None,
        governance_account_id: Optional[str | int] = None,
        status: Optional[str] = None,
        wasabi_account_name: Optional[str] = None,
        wasabi_account_number: Optional[str | int] = None,
        include_deleted: Optional[bool] = None,
        include_keys: Optional[bool] = None,
    ) -> Response:
        """GET /v1/sub-accounts"""

        params = {
            "page": page,
            "size": size,
            "id": id_,
            "name": name,
            "controlAccountId": control_account_id,
            "governanceAccountId": governance_account_id,
            "status": status,
            "wasabiAccountName": wasabi_account_name,
            "wasabiAccountNumber": wasabi_account_number,
            "includeDeleted": include_deleted,
            "includeKeys": include_keys,
        }
        return self._request("GET", "/v1/sub-accounts", params=params)

    def get_sub_account(
        self,
        sub_account_id: str | int,
        *,
        include_keys: Optional[bool] = None,
    ) -> Response:
        """GET /v1/sub-accounts/:subAccountId"""

        params = {"includeKeys": include_keys}
        path = f"/v1/sub-accounts/{sub_account_id}"
        return self._request("GET", path, params=params)

    def update_sub_account(
        self,
        sub_account_id: str | int,
        payload: Mapping[str, Any],
        *,
        include_keys: Optional[bool] = None,
    ) -> Response:
        """PUT /v1/sub-accounts/:id"""

        params = {"includeKeys": include_keys}
        path = f"/v1/sub-accounts/{sub_account_id}"
        return self._request("PUT", path, params=params, json=payload)

    def patch_sub_account(
        self,
        sub_account_id: str | int,
        payload: Mapping[str, Any],
        *,
        include_keys: Optional[bool] = None,
    ) -> Response:
        """PATCH /v1/sub-accounts/:id"""

        params = {"includeKeys": include_keys}
        path = f"/v1/sub-accounts/{sub_account_id}"
        return self._request("PATCH", path, params=params, json=payload)

    def delete_sub_account(self, sub_account_id: str | int) -> Response:
        """DELETE /v1/sub-accounts/:id"""

        path = f"/v1/sub-accounts/{sub_account_id}"
        return self._request("DELETE", path)


__all__ = ["SubAccountEndpoints"]
