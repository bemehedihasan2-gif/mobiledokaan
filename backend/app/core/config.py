from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: str = "development"
    app_secret_key: str = "change-me-in-production"
    app_name: str = "Mobiledokaan API"
    api_v1_prefix: str = "/api/v1"

    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/mobileaihub"

    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"

    gemini_api_key: str = ""
    gemini_api_keys: str = ""
    gemini_project_id: str = "default"
    gemini_model: str = "gemini-3.6"
    ai_default_provider: str = "gemini"
    ai_timeout_seconds: int = 60
    ai_max_retries: int = 2

    admin_username: str = "admin"
    admin_password: str = ""
    admin_password_hash: str = ""
    admin_token_ttl_seconds: int = 86400
    admin_auth_disabled: bool = False

    smtp_host: str = ""
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    smtp_from: str = ""
    smtp_use_tls: bool = True

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    @property
    def gemini_configured(self) -> bool:
        return bool(self.gemini_api_key and self.gemini_api_key.strip())

    @property
    def is_production(self) -> bool:
        return self.app_env.lower() == "production"

    def validate_production_safety(self) -> list[str]:
        issues: list[str] = []
        if self.is_production:
            if self.admin_auth_disabled:
                issues.append("ADMIN_AUTH_DISABLED must be false in production")
            if self.app_secret_key in ("", "change-me-in-production"):
                issues.append("APP_SECRET_KEY must be a strong unique value")
            if self.admin_password and not self.admin_password_hash:
                issues.append("Prefer ADMIN_PASSWORD_HASH over plain ADMIN_PASSWORD")
            if not self.cors_origins_list:
                issues.append("CORS_ORIGINS should list your production frontend origin")
            if "*" in self.cors_origins:
                issues.append("CORS must not use wildcard * in production")
            if len(self.app_secret_key) < 32:
                issues.append("APP_SECRET_KEY should be at least 32 characters")
        return issues


@lru_cache
def get_settings() -> Settings:
    return Settings()
