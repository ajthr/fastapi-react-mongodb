from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from bson.json_util import dumps
from bson.objectid import ObjectId

from core import db

router = APIRouter()
Items = db.items


class CreateItem(BaseModel):
    item_name: str
    item_description: str


class UpdateItem(BaseModel):
    id: str
    item_name: str
    item_description: str


class DeleteItem(BaseModel):
    id: str


@router.get("/")
def get_items():
    items = list(Items.find({}))
    if items is not None:
        return Response(content=dumps(items), status_code=200)
    return Response(content=dumps([]), status_code=204)


@router.post("/")
def create_item(data: CreateItem):
    if data:
        id = Items.insert_one(
            {"item_name": data.item_name, "item_description": data.item_description}).inserted_id
        return JSONResponse(content = { "id": str(id) }, status_code=200)
    return Response(status_code=204)


@router.patch("/")
def update_item(data: UpdateItem):
    if data:
        Items.update_one({"_id": ObjectId(data.id)},
                         {"$set":
                             {"item_name": data.item_name, "item_description": data.item_description}})
        return Response(status_code=200)
    return Response(status_code=204)


@router.delete("/")
def create_item(data: DeleteItem):
    if data:
        Items.delete_one({"_id": ObjectId(data.id)})
        return Response(status_code=200)
    return Response(status_code=204)
