"""FastAPI entry point for the SMS Surface service."""

import os
import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import settings
from src.scheduler import start_scheduler, stop_scheduler
from src.sms_handler import handle_inbound_sms

app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check for load balancers and monitoring."""
    return {"status": "ok", "service": settings.app_name}


@app.post("/sms/inbound", response_class=PlainTextResponse)
async def sms_inbound(request: Request) -> str:
    """Twilio webhook for incoming SMS messages."""
    return await handle_inbound_sms(request)


@app.get("/auth/callback")
async def auth_callback(code: str, state: str) -> dict[str, str]:
    """Keycloak OAuth callback.

    TODO: implement after Keycloak question is answered.
    """
    return {"status": "stub", "code": code, "state": state}


@app.on_event("startup")
async def startup() -> None:
    """Start background services when the app boots."""
    await start_scheduler()


@app.on_event("shutdown")
async def shutdown() -> None:
    """Clean up background services on shutdown."""
    await stop_scheduler()


def main() -> None:
    """Run the service with uvicorn."""
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=settings.debug)


if __name__ == "__main__":
    main()
