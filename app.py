import uuid
from flask import Flask,request
from db import stores, items

app = Flask(__name__)



@app.get("/store")
def get_all_stores():
    return {"stores":list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json() # Get the store data you want to create
    store_id  = uuid.uuid4().hex # generate unique id for the store

    new_store = {**store_data, "id": store_id } # unpack the storedata dictionary using
                                            # keyword unpacker ** and also give another 
                                            # key 'id'
    stores[store_id] = new_store
    return new_store,201

@app.post("/item") # We no longer create items inside store
def create_item():
    item_data = request.get_json()
    item_id = uuid.uuid4().hex
    if item_data['store_id'] not in stores:
        return {"message" : "Store not found"}, 404
    new_item = {**item_data, "id":item_id}
    items[item_id] = new_item
    return new_item,201

@app.get('/item')
def get_all_items():
    return { "items": list(items.values())}

@app.get("/store/<string:store_id>")
def get_single_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message" : "No such store found"},404

@app.get("/item/<string:item_id>")
def get_single_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message" : "No such store/item found"},404


    
    
