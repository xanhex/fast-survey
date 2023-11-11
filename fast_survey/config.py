"""App config."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App settings class."""

    app_name: str = 'fast-survey'
    title: str = 'Fast Survey API'
    summary: str = 'Microservice for user surveys.'
    items_per_user: int = 50
    database_url: str = 'mongodb://root:example@mongo:27017/'
    database_url_test: str = 'mongodb://root:example@localhost:27017/'
    testing: bool = False

    model_config = SettingsConfigDict(
        env_file='fast_survey/.env',
        extra='ignore',
    )


settings = Settings()
