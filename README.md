# cmugpt-sms-surface

SMS/iMessage companion feature for the [Bark Agent](https://git.cmu.dev/ScottyLabs/cmugpt-agent). Students send iMessages via [BlueBubbles](https://bluebubbles.app/), authenticate with their CMU Andrew ID, and chat with the CMU campus assistant for event notifications, schedule planning, reminders, and orientation-week help.

## Local setup

Install Lix and log in to OpenBao by following kennel's [local development](https://docs.kennel.scottylabs.org/guides/local-development/#installing-nix) and [secrets](https://docs.kennel.scottylabs.org/guides/secrets/#local-development) guides. Then enter the dev shell, which installs the dependencies, and start the service on `http://localhost:8000`:

```sh
nix develop
pitchfork start --local
```

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
│   ├── agent_client.py  # Boundary with the Bark agent (API or direct import)
│   └── scheduler.py     # Reminders + event notifications
```

## Planned integration with cmugpt-agent

- Mirrors `cmugpt-agent`'s stack: Python 3.12, FastAPI, `uv`, `ruff`, `ty`.
- Keeps all new code in this repo; `cmugpt-agent/` is read-only context.
- Talks to the agent through `src/agent_client.py`, which can be wired to either the agent's HTTP API or a direct Python import once that decision is finalized.

## Open questions before implementation

1. Should SMS call the agent API or import the agent package directly?
1. What database for production? (SQLite for MVP, then Postgres?)
1. What "basic student info" should be saved?
1. How does the CMU Keycloak auth flow work?
1. Where does orientation/week event data come from?
1. Should reminders be proactive or reactive in the MVP?
