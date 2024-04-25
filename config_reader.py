from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    DB_HOST: str
    DB_PORT: int
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: SecretStr
    DB_NAME: str
    COLLECTION_NAME: str
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


config = Settings()
