from core import api

from crud.crud_item import router

api.include_router(router, prefix="/items")
