from fastapi import APIRouter
app = APIRouter()
# QUERY PARAMETERS:

# if we are declaring anything other that are not part of path parameters i.e. after ?
# in the below code based on the value we provide in the url ex: skip 1 and limit 1 then 
# return items [1:2] which gives {name: "Bar"}
# all the quiey things are to be given along with = 

names = [{"name": "Foo"}, {"name": "Bar"}, {"name": "Com"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
   return items[skip : skip + limit]

# so URL : http://127.0.0.1:8000/items/?skip=0&limit=10



@app.get("/terms/{term_id}")
async def read_item(term_id: str, q: str, short: bool = False): # if q is required
# async def read_item(term_id: str, q: str | None = None, short: bool = False): # if not needed the q    
    item = {"term_id": term_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"} # if short is true, yes, on then this will display
        )
    return item


# QUERY PARAMETERS 2

@app.get("/items2/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    
    if q:
        results.update({"q": q})
    return results
