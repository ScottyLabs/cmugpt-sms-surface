"""FastAPI entry point for the SMS Surface service."""

import os
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import settings
from src.scheduler import start_scheduler, stop_scheduler
from src.sms_handler import handle_inbound_message


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    """Manage startup and shutdown lifecycle."""
    await start_scheduler()
    yield
    await stop_scheduler()


app = FastAPI(title=settings.app_name, debug=settings.debug, lifespan=lifespan)


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check for load balancers and monitoring."""
    return {"status": "ok", "service": settings.app_name}


@app.post("/message/inbound", response_class=JSONResponse)
async def message_inbound(request: Request) -> JSONResponse:
    """BlueBubbles webhook for incoming iMessage messages."""
    return await handle_inbound_message(request)


@app.get("/auth/callback")
async def auth_callback(code: str, state: str) -> dict[str, str]:
    """Keycloak OAuth callback.

    TODO: implement after Keycloak question is answered.
    """
    return {"status": "stub", "code": code, "state": state}


def main() -> None:
    """Run the service with uvicorn."""
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=settings.debug)


if __name__ == "__main__":
    main()
