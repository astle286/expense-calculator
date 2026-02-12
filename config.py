import os

class Config:
    # Secret key for session signing
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")

    # Database connection (default: Postgres in Docker)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@db:5432/expenses"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Prometheus / Monitoring toggle
    ENABLE_METRICS = os.environ.get("ENABLE_METRICS", "true").lower() == "true"

    # Logging
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
