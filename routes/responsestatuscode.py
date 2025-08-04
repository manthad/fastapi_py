from fastapi import APIRouter, Form

app = APIRouter()

@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
# no need to remember all the numbers if we use status. then system will assist


# FORM DATA: This is used if we want to get input from html form
# as we know fastapi always expects data to come in json format only

from typing import Annotated


app = APIRouter()

@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
# form fields not in json type

# FORM MODEL --- need to ask
class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"} # can also be used to exclude extra forms

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]): #here the form data we are considering it as form type
    return data

# REST FILES 
# import and upload files using fastapi

