"""CMU Keycloak authentication flow for SMS users.

TODO: implement OAuth2 / OIDC redirect and token exchange once
CMU Keycloak details are confirmed.
"""

from __future__ import annotations


async def build_auth_link(phone_number: str) -> str:
    """Return a URL that sends the user through CMU Keycloak login.

    TODO: implement after Keycloak question is answered.
    """
    del phone_number  # unused
    return "https://example.com/auth-placeholder"


async def handle_keycloak_callback(code: str, state: str) -> dict[str, str]:
    """Exchange the Keycloak authorization code for tokens and user info.

    TODO: implement after Keycloak question is answered.
    """
    del code, state  # unused
    return {"andrew_id": "TODO", "name": "TODO"}
