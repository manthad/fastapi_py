from fastapi import APIRouter # from fasapi framework we are importing FastAPI method
app = APIRouter() # creating an object as method is just a blue print

# ENUM - enumeration used to enter valid type of data and limit the values from a certain options.
from enum import Enum
class ModelName(str, Enum): # this is called a model which uses pydantic structure
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName): #this model is called here.instead of giving some random value we need to provide certain values
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



# FILE PATH

@app.get("/files/{file_path:path}") # here :path will allow us to provide the real filepath if we dont give it will take as a string only
async def read_file(file_path: str):
    return {"file_path": file_path}






