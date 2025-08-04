from fastapi import APIRouter # from fasapi framework we are importing FastAPI method
app = APIRouter() # creating an object as method is just a blue print

# GENERAL FUNCTION:

@app.get("/") # trying to get the data
async def root(): # this is an asynchronous function used here 
    return {"message": "Hello World"}


# PATH PARAMETERS:
@app.get("/items/{item_id}") # first items is slug- non changable and second one is pathe parameter
# async def read_item(item_id):
async def read_item(item_id: int):   # mentioning it to be specifically an int 
    return {"item_id": item_id}    

# ORDER 
# Sometimes the API has to validate data one after other i.e user name and then user id then we need to wrtie the code properly

@app.get("/users/name/{user}")
async def user_name(user: str):    
    return {"user": user} 

@app.get("/users/id/{id}")
async def user_id(id: int):    
    return {"id": id} 

# Here if i use both as /users/{user} and /user/{id} as for both the path is same it will consider only first one and then not 
# validate the second one




