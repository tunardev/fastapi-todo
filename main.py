from fastapi import FastAPI
from pydantic import BaseModel
from repository import UserRepository

app = FastAPI()
db = UserRepository()

class User(BaseModel):
    username: str
    password: str

@app.get("/")
def find_users():
    users = db.find_users()
    
    return { 'data': users, 'status_code': 200 }

@app.post("/")
def create_user(user: User):
    user = db.insert_user(user.username, user.password)
    
    return { 'data': user, 'status_code': 200 }

@app.get("/{username}")
def find_user(username: str):
    user = db.find_user(username)
    
    if user:
        return { 'data': user, 'status_code': 200 }
    else:
        return { 'message': 'user not found', 'status_code': 403 }

@app.put("/{username}")
def update_user(username: str, user: User):
    user = db.update_user(username, user.username, user.password)
    
    return { 'data': user, 'status_code': 200 }

@app.delete('/{username}')
def delete_user(username: str):
    success = db.delete_one(username)
    
    return { 'data': success, 'status_code': 200 }