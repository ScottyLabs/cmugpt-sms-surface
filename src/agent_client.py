"""Integration boundary with the CMUGPT agent.

This module keeps the SMS service decoupled from the agent's internals.
After answering the integration question, implement either:

1. API client mode: POST to `agent_api_url` with the user's message.
2. Direct import mode: import `agent` from the sibling `cmugpt-agent` package.

For now it exposes a stub interface so the rest of the app can compile.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.config import settings


@dataclass
class AgentResponse:
    """Normalized response from the CMUGPT agent."""

    text: str
    action: str = "respond"


async def ask_agent(query: str, user_id: str | None = None) -> AgentResponse:
    """Send a student message to the agent and return the reply.

    TODO: implement once the integration question is answered.
    """
    if settings.agent_direct_import:
        return await _ask_via_import(query, user_id)
    return await _ask_via_api(query, user_id)


async def _ask_via_api(query: str, user_id: str | None = None) -> AgentResponse:
    """Call the cmugpt-agent HTTP API."""
    # Placeholder: replace with real httpx call after agent_api_url is set.
    del query, user_id  # unused
    return AgentResponse(text="Hello from SMS Surface! (agent API stub)")


async def _ask_via_import(query: str, user_id: str | None = None) -> AgentResponse:
    """Import and run the agent package directly."""
    # Placeholder: replace with `from agent import run_agent` after sys.path setup.
    del query, user_id  # unused
    return AgentResponse(text="Hello from SMS Surface! (agent import stub)")
