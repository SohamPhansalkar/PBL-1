from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware 

import User

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class UserRequest(BaseModel):
    email: str
    password: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the PBL-1 API"}

@app.post("/signup")
def signup_endpoint(user: UserRequest):
    result = User.signUp(user.email, user.password)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.post("/login")
def login_endpoint(user: UserRequest):
    result = User.logIn(user.email, user.password)
    if result["status"] == "error":
        raise HTTPException(status_code=401, detail=result["message"])
    return result