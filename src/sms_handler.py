"""BlueBubbles iMessage inbound/outbound handling.

TODO: implement message parsing, session state lookup, and reply sending
after the auth and DB questions are answered.
"""

from __future__ import annotations

import httpx
from fastapi import Request
from fastapi.responses import JSONResponse

from src.config import settings


async def handle_inbound_message(request: Request) -> JSONResponse:
    """Process a BlueBubbles webhook payload and return an acknowledgement.

    TODO: replace stub with real flow once auth + DB are ready.
    """
    payload = await request.json()
    body = str(payload.get("text", "")).strip()
    from_handle = payload.get("handle", "")
    chat_guid = payload.get("chatGuid", "")

    # Placeholder: look up user, authenticate if needed, then ask agent.
    reply = f"You said: {body}. (BlueBubbles handler stub)"
    if settings.debug:
        reply += f" [from {from_handle}, chat {chat_guid}]"

    await send_bluebubbles_message(chat_guid, reply)
    return JSONResponse({"status": "delivered", "reply": reply})


async def send_bluebubbles_message(chat_guid: str, message: str) -> None:
    """Send an iMessage via the BlueBubbles server REST API."""
    if not settings.bluebubbles_url:
        return

    url = f"{settings.bluebubbles_url.rstrip('/')}/api/v1/message"
    headers: dict[str, str] = {}
    if settings.bluebubbles_password:
        headers["Authorization"] = settings.bluebubbles_password

    payload = {
        "chatGuid": chat_guid or settings.bluebubbles_chat_guid,
        "message": message,
    }

    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload, headers=headers)


async def handle_outbound_sms(to_number: str, message: str) -> None:
    """Send a proactive message.

    TODO: implement after chat routing and proactive vs reactive
    question are answered.
    """
    del to_number, message  # unused
