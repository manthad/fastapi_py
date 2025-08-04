from fastapi import APIRouter, Query
from fastapi import Path
from pydantic import BaseModel

app = APIRouter()

# QUERY PARAMETERS AND STRING VALIDATION

from typing import Annotated

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=10)] = None):
# async def read_items(q: Annotated[str | None, Query(min_lenght=3, max_length=10, pattern="^fixedquery$")] = None):
# async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery") # here query is not optional # if we want some default value with fixed length
                                                                            # only matches for fixedquery as both the symbols are start and stop of word
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


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
   return {} 


# async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str): # just like print in python to describe what should give on url thats it
                                                                                    

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









