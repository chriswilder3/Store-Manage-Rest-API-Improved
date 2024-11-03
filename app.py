import uuid
from flask import Flask,request
from db import stores, items
from flask_smorest import abort

app = Flask(__name__)


@app.get("/")
def home_page():
    return "<h1> Connected Successfully </h1>"

@app.get("/store")
def get_all_stores():
    return {"stores":list(stores.values())}

@app.get("/store/<string:store_id>")
def get_single_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message = "No such Store Id exists")

@app.post("/store")
def create_store():
    store_data = request.get_json() # Get the store data you want to create
    if "name" not in store_data:
        abort(400, message=" 'name' field doesnt exist in JSON ")
    
    for store in stores.values():
        if store['name'] == store_data['name']:
            abort(400, message= " store with this name already exists")
    store_id  = uuid.uuid4().hex # generate unique id for the store

    new_store = {**store_data, "id": store_id } # unpack the storedata dictionary using
                                            # keyword unpacker ** and also give another 
                                            # key 'id'
    stores[store_id] = new_store
    return new_store,201

@app.delete('/store/<string:store_id>')
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message" : "Deleted Successfully"}
    except KeyError:
        abort(404, message=" store ID not found")


@app.put('/store/<string:store_id>')
def update_store(store_id): 
    store_data = request.get_json() # We are expecting json with new data
                                   # : name and price. for simplicity 
                                   # store_id cant be updated.
    if 'name' not in store_data:
        abort(400, message=" 'name' is necessary in json ")
    try:
        store = stores[store_id] # Get the particular item in items Dict.
        store |= stores_data # This is called as dictionary update operator
                     # It is same as a = a | b. it is able to merge dict with 
                     # new data as long as this new data forms part of dict.
        return store
        return {"message" : "updated Successfully"}
    except KeyError:
        abort(404, message=" store ID not found")

@app.post("/item") # We no longer create items inside store
def create_item():
    # Here, in addition to ensuring that all fields are passes in the data
    # We also need to verify the correctness of each field datatype.
    # Ex : price must be float, name must be string etc
    # This process is called Data validation in APIs.
    # we use the marshmellow library for this.
    item_data = request.get_json()
    if ("price" not in item_data or
        "store_id" not in item_data or
        "name" not in item_data):
        abort(400, message="Bad request. Make sure price/store_id/name exist in the data")
    
    for item in items.values(): # This checks for duplicate elements being added ( same name item being added at same store )
        if (item_data['name'] == item['name'] and
             item_data['store_id'] ==items['store_id']):
             abort(400, message=" Item already exists")
    
    if item_data['store_id'] not in stores:
       abort(404, message=" Item doesn't exist in any known stores") 

    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id":item_id}
    items[item_id] = new_item
    return new_item,201

@app.put('/item/<string:item_id>')
def update_item(item_id): 
    item_data = request.get_json() # We are expecting json with new data
                                   # : name and price. for simplicity 
                                   # store_id cant be updated.
    if 'price' not in item_data or 'name' not in item_data:
        abort(400, message=" 'name' and 'price' are necessary in json ")
    try:
        item = items[item_id] # Get the particular item in items Dict.
        item |= item_data # This is called as dictionary update operator
                     # It is same as a = a | b. it is able to merge dict with 
                     # new data as long as this new data forms part of dict.
        return item
        return {"message" : "updated Successfully"}
    except KeyError:
        abort(404, message=" Item ID not found")

@app.delete('/item/<string:item_id>')
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message" : "Deleted Successfully"}
    except KeyError:
        abort(404, message=" Item ID not found")


@app.get('/item')
def get_all_items():
    return { "items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_single_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message= "No such item Id exists")
