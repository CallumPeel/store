import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)

# Item APIs ******************************************************

# NEEDS WORK
@app.post("/item")
def create_item():
    item_data = request.get_json()
    item_id = item_data["store_id"]
    print("hello123")
    print(item_data["store_id"])
    print("hello")
    if item_data["store_id"] not in stores:
        return {"message": "Item not in stores"}, 401
    item_id = uuid.uuid4().hex
    new_item = {**item_data, "item_id": item_id}
    items[item_id] = new_item
    return new_item, 201


@app.get("/item")
def get_items():
    return {"Items": list(items.values())}, 201


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item was not found."}, 404


# Store APIs ***********************************************************

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "store_id": store_id}
    stores[store_id] = new_store
    return new_store, 201

@app.get("/store")
def get_stores():
    return {"Stores": list(stores.values())}, 201


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Error, Store not found"}, 404

