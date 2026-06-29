"""Background scheduling for reminders and event notifications.

TODO: implement after proactive vs reactive question and event data source
question are answered.
"""

from __future__ import annotations

from apscheduler.schedulers.asyncio import AsyncIOScheduler

_scheduler: AsyncIOScheduler | None = None


def get_scheduler() -> AsyncIOScheduler:
    """Return the global scheduler instance, creating it if necessary."""
    global _scheduler
    if _scheduler is None:
        _scheduler = AsyncIOScheduler()
    return _scheduler


async def start_scheduler() -> None:
    """Start the background scheduler."""
    get_scheduler().start()


async def stop_scheduler() -> None:
    """Stop the background scheduler."""
    if _scheduler is not None:
        _scheduler.shutdown()


def schedule_reminder(user_id: str, content: str, when: str) -> None:
    """Schedule a one-time reminder to be sent to a user.

    TODO: implement after reminder design is finalized.
    """
    del user_id, content, when  # unused
