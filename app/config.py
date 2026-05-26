"""Application configuration."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables."""

    app_name: str = "Mainframe Application Intelligence Platform"
    app_env: str = "local"

    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/mainframe_intelligence"

    chroma_path: str = ".chroma"
    chroma_collection: str = "mainframe_chunks"

    google_cloud_project: str | None = None
    google_cloud_location: str = "us-central1"
    vertex_model_name: str = "gemini-1.5-pro"
    embedding_model_name: str = "text-embedding-004"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
