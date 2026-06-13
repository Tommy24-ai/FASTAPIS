# from fastapi import FastAPI
# app = FastAPI()
# @app.post("/createuser")
# def create_user(name:str, age:int):
#     return{"message": "User created successfully", "data": {"name": name, "age": age}}


###########################################################################################

from fastapi import FastAPI
app = FastAPI()
@app.post("/createuser")
def create_user(name:str, age:int,clg:str,sem:int):
   return{"message": "User created successfully", "data": {"name": name, "age": age, "clg": clg, "sem": sem}}