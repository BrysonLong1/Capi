from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str = "production"
    SECRET_KEY: str = "change_me"
    LOG_LEVEL: str = "INFO"
    BRIDGE_DOMAIN: str = "https://tickets.trovixnights.com"

    REDIS_URL: str = "redis://127.0.0.1:6379/0"
    DATABASE_URL: str = "sqlite:///bridge.db"
    RATE_LIMIT_RPM: int = 60

    ALLOWED_QUERY_KEYS: str = "fbclid,ttclid,gclid,wbraid,gbraid,utm_source,utm_medium,utm_campaign,utm_content,utm_term,cid,evt"

    FB_PIXEL_ID: str = ""
    FB_ACCESS_TOKEN: str = ""
    FB_TEST_EVENT_CODE: str | None = None
    FB_API_VERSION: str = "v19.0"

    GA4_MEASUREMENT_ID: str = ""
    GA4_API_SECRET: str = ""
    DEFAULT_UTM_SOURCE: str = "meta"
    DEFAULT_UTM_MEDIUM: str = "paid-social"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
