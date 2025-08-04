from fastapi import FastAPI
app = FastAPI()

# GENERAL FUNCTION:

@app.get("/")
async def root():
    return {"message": "Hello World"}



# PATH PARAMETERS:
@app.get("/items/{item_id}")
# async def read_item(item_id):
async def read_item(item_id: int):    
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
#   validate the second one



# ENUM
from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



# FILE PATH

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# QUERY PARAMETERS:

# if we are declaring anything other that are not part of path parameters i.e. after ?
# in the below code based on the value we provide in the url ex: skip 1 and limit 1 then 
# return items [1:2] which gives {name: "Bar"}
# all the quiey things are to be given along with = 

items = [{"name": "Foo"}, {"name": "Bar"}, {"name": "Com"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
   return items[skip : skip + limit]


@app.get("/terms/{term_id}")
async def read_item(term_id: str, q: str, short: bool = False): # if q is required
# async def read_item(term_id: str, q: str | None = None, short: bool = False): # if not needed the q    
    item = {"term_id": term_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# QUERY PARAMETERS 2


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    
    if q:
        results.update({"q": q})
    return results


# REQUEST BODY 
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# app = FastAPI()    
   

@app.post("/basemodel/")
async def create_item(item: Item):
    return item 

# for put

@app.put("/basemodel/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# if wanted to add query for the same above function then    

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()} # this is syntax shortcut for displaying all the values in dictionary form
    if q:
        result.update({"q": q})
    return result        

# QUERY PARAMETERS AND STRING VALIDATION

from typing import Annotated

from fastapi import FastAPI, Query

@app.get("/items5/")
async def read_items(q: Annotated[str | None, Query(max_length=10)] = None):
# async def read_items(q: Annotated[str | None, Query(min_lenght=3, max_length=10, pattern="^fixedquery$")] = None):
# async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery") # if we want some default value with fixed length
    # only matches for fixedquery as both the symbols are start and stop of word
    # or
# async def read_items(q: str | None = Query(default=None, max_length=50)):   
# if we want to declare a value as required inside query then dont declare a default value remove None from the prior line     
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
# this is for if we want to give query parameter and it shoul not exceed 50 length  
    if q:
        results.update({"q": q})
    return results  


async def read_items(q: Annotated[list[str] | None, Query()] = None):
    # can use list[str] or list also
    # if we wanted to use the q for several times then we can make it as list and the url canbe 
        # http://localhost:8000/items/?q=foo&q=bar
    return {} 


async def read_items(q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,):        
    # can add title and description also

# if i wnt my parameter like instead of q i need something like item_query then we need to put this in alias
# also if some one is using a parameter and it might be removed or updated in the future then u put it as depricated = True
# under query or it can be parameter
    return {} 
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):

# to exclude a query parameter from generated OPEN API schema - need to check

# Custome validator. - need to check 


   return {} 


# As we are validating the query parameters with many validations the same way we can validate the path parameters too


from fastapi import FastAPI, Path, Query

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
   return {} 


# async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str): # what is this
   

# ge=1 after the Path(title) which is greter or equal to 1
# gt=0, le=1000

#    return {} 
# can i write the name as whaterver i want for query parameter or should i mentone it in alias only
@app.get("/items6/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
   return {}


# EXTRA FORBID 
# pydantic model gives a feature of rejecting if user provides unnecessary query parameters

from typing import Annotated, Literal


class FilterParams(BaseModel):
    # model_config = {"extra": "forbid"}. # only this one line will do the work of forbidding

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

# BODY MULTIPLE PARAMETERS.
# means normalyy we only write one body but we can use many bodies    

async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):

    # here it will give normal json o/p only but with the parameter name also like item: { name......}

#   BODY - FIELDS

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
# here declaring in the body itself the conditions or oher validations

# BODY NESTED MODELS - defining attribute with subtype
 tags: list = [] # inside the class Item(basemodel)

 # now if we want to mention the list type as string or int then 
 from typing import List, Union

tax: Union[float, None] = None
    tags: List[str] = []

# SET TYPES:
tags: set[str] = set()    # this is set of strings. ex if the tags have duplicate values it will consider as unique

# NESTED MODELS
class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None # here image is taken from the above class Image

# sub model then the o/p is all the mentioned and then image with url and name in it like tree diagram

# special type is
from pydantic import BaseModel, HttpUrl
url: HttpUrl # this will validate URL

# Attributes with list of subtypes:
images: list[Image] | None = None # here image is again a class like previous topic
# listing means here we can provide any number of url and names which displays as set

# deeply. nested means just like image is used under item the item is again used in other class thats it

# Bodies of pure list

async def create_multiple_images(images: list[Image]): # here image is a class

# Editor support means when we are writing code and mentioning one thing in a line, in the next line it will remember and give us hints 
# if we want to improvise our code. like if i mentioned a as string then if a. then it will show title(), captialise() which are related


async def create_index_weights(weights: dict[int, float]): # explain


# Declare request example data
    1

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {        # this is replaced with class Config:
        "json_schema_extra": { # this schema_extra without ""
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

# we can declare additional example inthe code 
 name: str = Field(examples=["Foo"])




 # extra data types
 # not only the basic data types but can use different also

 UUID: - Uniersity unique identifier
 datetime.datetime: displays time in ISO 8601 format
 datetime.date, datetime.time, datetime.timedelta
 frozenset: treated as set in requests converts them if duplicate values to unique and list in response
 bytes:
 decimal:

 from datetime import datetime, time, timedelta

item_id: UUID,
    start_datetime: Annotated[datetime, Body()],

# cookie 
from fastapi import cookie    
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):

# header - main job is to tell fastapi to read specific value from request headers.
# generally http variables have names with - where python cannot have variable names with - so if we use this
# it will only convert the_ to the -. BDW it is also validation and conversion tool

async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
# if we dont want to convert the _ to - then
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):

# we can have duplicate headers i.e. one header can have different values
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):

# cookie parameter model.
# so declare all the values that are need as cookie parameters using pydantic model and can call them any no of times

class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
# the forbid can also be used here as above
# the same way if you have group of header parameters can place them in the same pydantic model


