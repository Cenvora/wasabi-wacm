"""Mixin containing WACM control account endpoints."""

from __future__ import annotations

from typing import Optional

from requests import Response

from ._base import EndpointMixin


class ControlAccountEndpoints(EndpointMixin):
    """Operations for `/v1/control-accounts` resources."""

    def get_control_account_usage(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        governance_account_id: Optional[str | int] = None,
        control_account_id: Optional[str | int] = None,
        latest: Optional[bool] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        wasabi_account_number: Optional[str | int] = None,
    ) -> Response:
        """GET /v1/control-accounts/usages"""

        params = {
            "page": page,
            "size": size,
            "governanceAccountId": governance_account_id,
            "controlAccountId": control_account_id,
            "latest": latest,
            "from": from_,
            "to": to,
            "wasabiAccountNumber": wasabi_account_number,
        }
        return self._request("GET", "/v1/control-accounts/usages", params=params)

    def get_control_accounts(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        name: Optional[str] = None,
        governance_account_id: Optional[str | int] = None,
        status: Optional[str] = None,
        primary_api_key: Optional[str] = None,
        include_api_key: Optional[bool] = None,
        id_: Optional[str | int] = None,
        control_account_email: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        include_deleted_sub_accounts: Optional[bool] = None,
    ) -> Response:
        """GET /v1/control-accounts"""

        params = {
            "page": page,
            "size": size,
            "name": name,
            "governanceAccountId": governance_account_id,
            "status": status,
            "primaryApiKey": primary_api_key,
            "includeApiKey": include_api_key,
            "id": id_,
            "controlAccountEmail": control_account_email,
            "includeDeleted": include_deleted,
            "includeDeletedSubAccounts": include_deleted_sub_accounts,
        }
        return self._request("GET", "/v1/control-accounts", params=params)

    def get_control_account(
        self,
        control_account_id: str | int,
        *,
        include_deleted: Optional[bool] = None,
        include_deleted_sub_accounts: Optional[bool] = None,
    ) -> Response:
        """GET /v1/control-accounts/:controlAccountId"""

        params = {
            "includeDeleted": include_deleted,
            "includeDeletedSubAccounts": include_deleted_sub_accounts,
        }
        path = f"/v1/control-accounts/{control_account_id}"
        return self._request("GET", path, params=params)

    def get_control_account_bucket_utilization(
        self,
        control_account_id: str | int,
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
        """GET /v1/control-accounts/:controlAccountId/buckets"""

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
        path = f"/v1/control-accounts/{control_account_id}/buckets"
        return self._request("GET", path, params=params)


__all__ = ["ControlAccountEndpoints"]
