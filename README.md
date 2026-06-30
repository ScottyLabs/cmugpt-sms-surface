# cmugpt-sms-surface

SMS/iMessage companion feature for the [CMUGPT Agent](https://github.com/ScottyLabs/cmugpt-agent). Students send iMessages via [BlueBubbles](https://bluebubbles.app/), authenticate with their CMU Andrew ID, and chat with the CMU campus assistant for event notifications, schedule planning, reminders, and orientation-week help.

## Local setup

1. Install dependencies with [`uv`](https://docs.astral.sh/uv/):

```sh
uv sync
```

2. Copy the example environment file and fill in your values:

```sh
cp .env.example .env
```

3. Run the service:

```sh
uv run python src/main.py
```

The app starts on `http://localhost:8000` by default.

## Development commands

- Format: `uv run ruff format`
- Lint: `uv run ruff check`
- Typecheck: `uv run ty check`
- Tests: `uv run pytest`

## Architecture

```
sms-surface/
├── src/
│   ├── main.py          # FastAPI app + webhook routes
│   ├── config.py        # Environment-based settings
│   ├── sms_handler.py   # BlueBubbles inbound/outbound iMessage logic
│   ├── auth.py          # CMU Keycloak integration
│   ├── database.py      # DB session + engine
│   ├── agent_client.py  # Boundary with CMUGPT agent (API or direct import)
│   └── scheduler.py     # Reminders + event notifications
```

## Planned integration with cmugpt-agent

- Mirrors `cmugpt-agent`'s stack: Python 3.12, FastAPI, `uv`, `ruff`, `ty`.
- Keeps all new code in this repo; `cmugpt-agent/` is read-only context.
- Talks to the agent through `src/agent_client.py`, which can be wired to either the agent's HTTP API or a direct Python import once that decision is finalized.

## Open questions before implementation

1. Should SMS call the agent API or import the agent package directly?
2. What database for production? (SQLite for MVP, then Postgres?)
3. What "basic student info" should be saved?
4. How does the CMU Keycloak auth flow work?
5. Where does orientation/week event data come from?
6. Should reminders be proactive or reactive in the MVP?
