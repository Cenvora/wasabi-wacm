"""High-level WACM API client composed from endpoint mixins."""

from __future__ import annotations

from .base import BaseWACMClient
from .endpoints import (
    ChannelAccountEndpoints,
    ControlAccountEndpoints,
    InvoiceEndpoints,
    MemberEndpoints,
    StandaloneAccountEndpoints,
    SubAccountEndpoints,
    UsageEndpoints,
)


class WACMClient(
    BaseWACMClient,
    SubAccountEndpoints,
    MemberEndpoints,
    ChannelAccountEndpoints,
    StandaloneAccountEndpoints,
    UsageEndpoints,
    InvoiceEndpoints,
    ControlAccountEndpoints,
):
    """Concrete client exposing all WACM API operations from the Postman collection."""


__all__ = ["WACMClient"]
