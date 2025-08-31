from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    open_router_base_url: str = ""
    open_router_deepseek_api_key: str = ""

    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    print(model_config.get("app_name"), "model_config")


settings = Settings()
