"""Configuration settings for the AI Story Creator backend."""
import os
from pathlib import Path
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


# Find project root directory (one level up from backend)
ROOT_DIR = Path(__file__).parent.parent.resolve()


class Settings(BaseSettings):
    """Application settings.
    
    This class manages all configuration settings for the application, sourced
    from environment variables with appropriate defaults where applicable.
    Environment variables are prefixed with 'aistory_'.
    """
    # Core application settings
    app_name: str = "AI Story Creator"
    debug: bool = False
    version: str = "0.1.0"
    api_prefix: str = "/api/v1"
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Database
    database_url: Optional[PostgresDsn] = None
    db_pool_size: int = 5
    db_max_overflow: int = 10
    db_echo: bool = False
    
    # Security
    secret_key: str = "CHANGE_ME_IN_PRODUCTION"  # Used for JWT encoding/decoding
    access_token_expire_minutes: int = 60 * 24 * 8  # 8 days
    algorithm: str = "HS256"
    
    # CORS
    cors_origins: List[AnyHttpUrl] = []
    cors_allow_credentials: bool = True
    cors_allow_methods: List[str] = ["*"]
    cors_allow_headers: List[str] = ["*"]
    
    # Rate limiting
    rate_limit_enabled: bool = True
    rate_limit_requests_per_minute: int = 60
    
    # Cache
    cache_enabled: bool = True
    cache_ttl_seconds: int = 60
    
    # Logging
    log_level: str = "INFO"
    
    # AI Service
    ai_service_url: Optional[AnyHttpUrl] = None
    ai_service_api_key: Optional[str] = None
    
    # File storage
    storage_backend: str = "local"  # Options: local, s3
    storage_local_path: str = "./uploads"
    storage_s3_bucket: Optional[str] = None
    storage_s3_region: Optional[str] = None
    
    model_config = SettingsConfigDict(
        # Look for .env file in project root directory
        env_file=os.path.join(ROOT_DIR, '.env'),
        env_file_encoding='utf-8',
        env_prefix='aistory_',
        extra='ignore',
        case_sensitive=False,
    )
    
    @field_validator("cors_origins", mode="before")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        """Parse CORS origins from string to list if provided as comma-separated string."""
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    @field_validator("database_url", mode="before")
    def assemble_db_connection(cls, v: Optional[str]) -> Optional[str]:
        """Ensure DB URL is properly formatted for SQLAlchemy."""
        if isinstance(v, str) and v.startswith("postgres://"):
            # Replace 'postgres://' with 'postgresql://' for SQLAlchemy 2.0+
            return v.replace("postgres://", "postgresql://", 1)
        return v


# Create a global instance of the settings
settings = Settings()


def get_settings() -> Settings:
    """Return the settings object as a dependency."""
    return settings