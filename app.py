import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request.data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request.data["name"], "price": request.data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Error, Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404
