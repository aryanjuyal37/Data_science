from fastapi import FastAPI, Path,Query,HTTPException, status
from typing import Optional 
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price:float 
    brand:Optional[str]=None

class UpdateItem(BaseModel):
    name:Optional[str] =None
    price:Optional[float] =None
    brand:Optional[str]=None

app= FastAPI() #object for fast api

# @app.get("/") #setting an end point
# def home():
#     return {"Data":"Testing"} 

# @app.get("/about")
# def about():
#     return {"Data":"About"}

# inventory={
#     1:{
#         "name":"Milk",
#         "price":45,
#         "brand":"Amul",
#     }
# }

inventory={} # to directly insert the item

# @app.get("/get-item/{item_id}/{name}") # user can input their choice in the endpoint to access data
# def get_item(item_id :int, name :str): # type hint in python to tell fastapi its an integer otherwise it will get an error when input is not integer
#     return inventory[item_id] 

@app.get("/get-item/{item_id}") # user can input their choice in the endpoint to access data
def get_item(item_id: int = Path (None,description="The id of the item u would like to view",gt=0)):# path adds details and description for what to type in for the user
#  None is the default value that always needs to be set and  setting gt=0 and lt=2 means the value inserted must be greater than 0 and less than 2
    return inventory[item_id] # le less than or equal and ge greater than equal 

# @app.get("/get-by-name")# one query parameter that we want to retrieve is accepted
# def get_item(name:Optional[str]=None):# here name is a required query parameter we can make it optional by making it equal to none  and there wont be an error
#     for item_id in inventory:
#         if inventory[item_id]["name"]==name:
#              return inventory[item_id]
#     return {"Data":"Not found"}


# @app.get("/get-by-name")# one query parameter that we want to retrieve is accepted
# def get_item(test :int,name:Optional[str]=None):# here we have test as a mandatory query paramter also mandatory ones shoud be declared before optional one 
#     for item_id in inventory:   
#         if inventory[item_id]["name"]==name:
#              return inventory[item_id]
#     return {"Data":"Not found"}


# @app.get("/get-by-name/{item_id}")# one query parameter that we want to retrieve is accepted
# def get_item(item_id:int,test :int,name:Optional[str]=None):# item_id also added as a mandatory parameter 
#     for item_id in inventory:   
#         if inventory[item_id]["name"]==name:
#              return inventory[item_id]
#     return {"Data":"Not found"}

# @app.post("/create-item/{item_id}") #add info to database with new endppoint method 
# def create_item(item_id:int ,item: Item): # request info body related to the item path paramters
#     if item_id in inventory:
#         return {"Error": "Item Id already exists "}

#     inventory[item_id]={"name":item.name, "brand":item.brand, "price":item.price}
#     return inventory[item_id]


@app.get("/get-by-name")# one query parameter that we want to retrieve is accepted
def get_item(name:str= Query(None, title="Name",description="Name of item",max_Length=20,min_Length=2)):# item_id also added as a mandatory parameter 
    for item_id in inventory:   
        if inventory[item_id].name==name:
             return inventory[item_id]
    # return {"Data":"Not found"}
    raise HTTPException(status_code=404, detail="Item ID not found")#in fast api waiting for heses exceptions and raises an http exception


@app.post("/create-item/{item_id}") #add info to database with new endppoint method 
def create_item(item_id:int ,item: Item): # request info body related to the item path paramters
    if item_id in inventory:
        # return {"Error": "Item Id already exists "}
        raise HTTPException(status_code=400, detail="Item ID already exists")

    inventory[item_id]=item
    return inventory[item_id]


@app.put("/update-item/{item_id}")#update item
def update_item(item_id:int,item:UpdateItem):#parameters using update item class
    if item_id not in inventory:
        # return {"Error": "Item Id does not exists "}
        raise HTTPException(status_code=404, detail="Item ID does not exist")
    if item.name != None:
        inventory[item_id].name=item.name#take item and it will update the item we have it will only update only whatu pass
    if item.price != None:
        inventory[item_id].price=item.price
    if item.brand != None:
        inventory[item_id].brand=item.brand

    return inventory[item_id]

@app.delete("/delete-item")
def del_item(item_id:int= Query(...,description="The ID of the item to delete",ge=0)):
    if item_id not in inventory:
        # return {"Error : Item Id does not exist"}
        raise HTTPException(status_code=404, detail="Item ID does not exist")

    if item.name != None:
        del inventory[item_id] # delete the  item
        return {"Success":"Item Deleted!"}