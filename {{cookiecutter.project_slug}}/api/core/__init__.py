from fastapi import FastAPI
from pymongo import MongoClient

from core.config import settings

database_client = MongoClient(settings.MONGO_DATABASE_URL)
db = database_client.{{ cookiecutter.mongodb_database }}

api = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/docs",
)
