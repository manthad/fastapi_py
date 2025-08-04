from fastapi import APIRouter
app = APIRouter()

# REQUEST BODY 
# now here comes post operation where we cannot see using url but only via docs or some ui in json format
# here we also send the request in json format only for that pydantic model is prefered.
# here we are creating data so what data we are creating need to be mentioned in the basemodel else it is a normal class
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/basemodel/")
async def create_item(item: Item): # we are creating the data from the Item
    return item 


# for put

@app.put("/basemodel/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()} # here will return all the Item values in dictionary format like keys and values

# if wanted to add query for the same above function then    

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result        

