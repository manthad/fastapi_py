from typing import Any
from pydantic import BaseModel, EmailStr
# not only for th response body i.e.input we provide conditions for the params 
#but we can alos provide conditions of how the o/p should look like
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = APIRouter()




@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

# here as we have both post and get so based on whatever fucntionlaity u are using it will give o/p
# if u use swaggger docs then post data is seen and url get data is seen thats it

# RESPONSE MODEL
@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item

# @app.get("/items/", response_model=list[Item])
# async def read_items() -> Any:
#     return item

# so normally it will retrn item type but what if the user provide wrong data like instead of float he provides string
# then this will throw error stating this is not the correct type
# also if extra params are provided it will not accept    


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
# here it works like we are providing user and pwd but during response we need only pwd so thats why we are writing it seperatly
# which is the good practice. Also while mentioning the response_model as UserOut it will only consider that.    
# this response model can be also treated like a filter for the response body

# another type

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

# Here eventhough it is considering all the input fields from baseuser and usein but as we have mentioned
# type -> Baseuser so only that data is returned

# RETURN A RESPONSE DIRECTLY

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

# here the ?teleport = false /true if false gives message else will open the link mentioned of the youtube which means response is directly seen
@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ") # this also can be used directly

# we cannot write -> Response | dict: cannot have 2 options
# but if we want to inore the response then we can put ,ike response_model = None after /portal under app.get

# not default response

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True) # can also use exclude_defaults = True or exclude_none =True
async def read_item(item_id: str):
    return items[item_id]
# here for example if the user provides a string value in url like foo. it will display response for name and price as mentioned
# Foo and tax = 50.2 instead of 10.5 eventhough it is default because we are using response_model_exclude thing


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]

# here in app.ge we mentioned include name and description hence we only get that data if we metioned exclude name excecpt that
# all data will be seen    


