from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application configuration loaded from environment variables
    DATABASE_URL: str

    # Load variables from the backend .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


# Shared application settings instance
settings = Settings()