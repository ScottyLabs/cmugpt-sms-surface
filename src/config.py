"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All runtime configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "SMS Surface"
    debug: bool = False

    # Twilio
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    twilio_phone_number: str = ""

    # CMUGPT Agent integration
    # TODO: choose one after answering the agent-integration question.
    agent_api_url: str = ""  # e.g. http://localhost:5000/agent/respond
    agent_api_key: str = ""  # shared secret if calling the agent API
    agent_direct_import: bool = False  # set True to import `agent` package directly

    # Auth
    # TODO: fill in after CMU Keycloak details are confirmed.
    cmu_keycloak_url: str = ""
    cmu_keycloak_client_id: str = ""
    cmu_keycloak_client_secret: str = ""

    # Database
    # TODO: switch to Postgres URL once production DB is decided.
    database_url: str = "sqlite:///./sms_surface.db"


settings = Settings()
