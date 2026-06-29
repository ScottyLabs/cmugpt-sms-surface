"""Twilio inbound/outbound SMS handling.

TODO: implement message parsing, session state lookup, and reply sending
after the auth and DB questions are answered.
"""

from __future__ import annotations

from fastapi import Request

from src.config import settings


async def handle_inbound_sms(request: Request) -> str:
    """Process a Twilio webhook payload and return the TwiML response.

    TODO: replace stub with real flow once auth + DB are ready.
    """
    form = await request.form()
    from_number = form.get("From", "")
    body = str(form.get("Body", "")).strip()

    # Placeholder: look up user, authenticate if needed, then ask agent.
    reply = f"You said: {body}. (SMS handler stub)"
    if settings.debug:
        reply += f" [from {from_number}]"

    return _twiml_response(reply)


def _twiml_response(message: str) -> str:
    """Build a minimal TwiML XML string for a single SMS reply."""
    escaped = message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        "<Response>"
        f"<Message>{escaped}</Message>"
        "</Response>"
    )


async def handle_outbound_sms(to_number: str, message: str) -> None:
    """Send a proactive SMS.

    TODO: implement after Twilio credentials and proactive vs reactive
    question are answered.
    """
    del to_number, message  # unused
