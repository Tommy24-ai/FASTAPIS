# dynamic URL

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/users/{user_id}")
# def user(user_id:int):
#     return {"user_id": user_id}
# ###########################################################################################
# query parameters

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/users/")
# def read_users(name:str=None):
#     return {"name": name}

# ###########################################################################################
#double parametere

from fastapi import FastAPI
app = FastAPI()
@app.get("/items/")
def get_items(name :str=None, Price: int =0):
    return {"name": name, "Price": Price}

#########################################################################################

