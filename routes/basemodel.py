from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Annotated
from typing import Annotated, Literal

app = APIRouter()

# EXTRA FORBID 

# pydantic model gives a feature of rejecting if user provides unnecessary query parameters



class FilterParams(BaseModel):
    model_config = {"extra": "forbid"} # only this one line will do the work of forbidding

    limit: int = Field(100, gt=0, le=100) # for adding extra validations in body parameters
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at" # either it has to order by one of the values provided 
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]): 

    return filter_query
# here if we write filterquery: FilterParams then it is assumed as body data but when u provide query() then it treats the FilterParams as query params

# BODY MULTIPLE PARAMETERS.
# means normalyy we only write one body but we can use many bodies    

# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):

    # here it will give normal json o/p only but with the parameter name also like item: { name......}




#   BODY - FIELDS

from typing import List, Union
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
                                     # here declaring in the body itself the conditions or oher validations

# BODY NESTED MODELS - defining attribute with subtype
    # tags: list = [] # inside the class Item(basemodel)

 # now if we want to mention the list type as string or int then 
 

    # tax: Union[float, None] = None
    tags: List[str] = []

# SET TYPES:
# tags: set[str] = set()    # this is set of strings. ex if the tags have duplicate values it will consider as unique but no order opp is list

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

# Deeply nested means just like image is used under item the item is again used in other class thats it

# Bodies of pure list

# async def create_multiple_images(images: list[Image]): # here image is a class

# Editor support means when we are writing code and mentioning one thing in a line, in the next line it will remember and give us hints 
# if we want to improvise our code. like if i mentioned a as string then if a. then it will show title(), captialise() which are related


# async def create_index_weights(weights: dict[int, float]): # here the keys are int and values are float 1: 20.5

from datetime import datetime, time, timedelta

# Declare request example data

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {        # this is replaced with class Config:   # this is used to forbid values, remove white spaces and correct validations of pydantic model
        "json_schema_extra": { # this schema_extra without ""
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,         # its like they are already providing data but if we want we can modify and validate
                }
            ]
        }
    }

# we can declare additional example in the code 

    name: str = Field(examples=["Foo"])




 # extra data types
 # not only the basic data types but can use different also

    # UUID: #- University unique identifier
    # datetime.datetime: #displays time in ISO 8601 format
    # datetime.date, datetime.time, datetime.timedelta
    # frozenset: #treated as set in requests converts them if duplicate values to unique and list in response
    # bytes:
    # decimal:


# item_id: UUID,
    start_datetime: Annotated[datetime, Body()],

# cookie 
from fastapi import cookie 

# async def read_items(ads_id: Annotated[str | None, Cookie()] = None):

# header - main job is to tell fastapi to read specific value from request headers.
# generally http variables have names with - where python cannot have variable names with - so if we use this
# it will only convert the_ to the -. BDW it is also validation and conversion tool

async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
# if we dont want to convert the _ to - then
# async def read_items(
#     strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
# ):

# we can have duplicate headers i.e. one header can have different values
# async def read_items(x_token: Annotated[list[str] | None, Header()] = None):

# cookie parameter model.
# so declare all the values that are need as cookie parameters using pydantic model and can call them any no of times

class Cookies(BaseModel):
    model_config = {"extra": "forbid"} 
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
# the forbid can also be used here as above
# the same way if you have group of header parameters can place them in the same pydantic model


