from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

app = APIRouter()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None

def fake_password_hasher(raw_password: str): # here we are creating a password masking function
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn): # now another function for taking the userin for password masking
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password) # here we are putting the userin data including the hashed 
                                                                            # pwd in userindb like a dict
    print("User saved! ..not really")
    return user_in_db

@app.post("/user/", response_model=UserOut) # here creating data 
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

 # we can use that inheritence concept for the same code like and rest all fucntionality is same
 class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(UserBase):
    password: str

class UserDB(UserBase):
    password: str

# UNION or anyOF - more optimized
@app.get("/items/{item_id}", response_model=Union[UserIn, UserDB])
@app.get("/items/", response_model=list[Item]) # can also write list in request_model also
@app.get("/items/", response_model=dict[str,float])

