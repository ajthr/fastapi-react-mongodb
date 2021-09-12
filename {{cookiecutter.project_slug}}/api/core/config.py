import os


class Settings:
    PROJECT_NAME = "{{ cookiecutter.project_slug }}"
    MONGO_DATABASE_URL = os.environ.get("DB_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")

settings = Settings()
