from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}
@app.get("/login")
def login():
    return {"message": "Login endpoint"}
@app.get("/register")
def register():
    return {"message": "Register endpoint"}
@app.get("/profile")
def profile():
    return{"message":"profile endpoint"}
@app.get("/logout")
def logout():
    return{"message":"Logout endpoint"}
