# REST FILES 
# import and upload files using fastapi

from typing import Annotated
from fastapi import APIRouter, File, Form, UploadFile

app = APIRouter()

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]): # if want multiple file uploads then use List[bytes] or List[UploadFile]
    return {"file_size": len(file)} #same with multiple uploads we can also give descriptions

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# the above both are used to upload files only
# File() is used for small files and gives only len(file) and reads it in bytes, while UploadFile is used for larger files 
# it will only give the filename or type of the content and allows you to read the file in chunks

# OPTIONAL FILES
# if you want to make the file upload optional, you can use the Optional type from typing

async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
# we can also write file description
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    file: Annotated[UploadFile, File(description="A file read as UploadFile")] 
    # it is like a description on the button field where we upload the file 


# FILE AND FORM:

# from typing import Annotated

# app = APIRouter()


# @app.post("/files/")
# async def create_file(
#     file: Annotated[bytes, File()],
#     fileb: Annotated[UploadFile, File()],
#     token: Annotated[str, Form()],
# ):
#     return {
#         "file_size": len(file),
#         "token": token,  # need to ask 
#         "fileb_content_type": fileb.content_type,
#     }