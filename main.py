from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

class User(BaseModel):
    name: str
    age: int
dic = [{"name": "Niv", "age": 26},
       {"name": "Niv", "age": 27}]    

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.post("/createNewUser")
def create_user(user: User):
    new_user = {"name": user.name, "age": user.age}
    dic.append(new_user)
    
    return dic

@app.delete("/deleteUser")
def delete_user(user: User):
    global dic
    old_dic_len = len(dic)
    dic = [u for u in dic if not (u["name"] == user.name and u["age"] == user.age)]
    if old_dic_len == len(dic):
        return {"message": "User not deleted",
                "remaining": dic}
    else:
        return {"message": "User deleted",
                "remaining": dic}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
