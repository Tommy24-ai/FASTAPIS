from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Adress(BaseModel):
    city: str
    state: str
class User(BaseModel):
    name: str
    age: int
    adress: Adress # linking with above class 
@app.post("/crreateuser")
def create_user(user: User):
    return user
