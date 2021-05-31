from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

class Todo(BaseModel):

    name: str
    email: str
    password: str
    phone:str

app = FastAPI(title="Todo API")

list_data = []

@app.get('/')
async def home():
    return {"Hello": "World"}

#CREATE
@app.post('/todo/')
async def create_todo(todo: Todo):
    list_data.append(todo)
    return todo

#READ ALL DATA
@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return list_data

#READ DATA BY ID
@app.get('/todo/{id}')
async def get_todo(id: int):

    try:        
        return list_data[id]   
    except:        
        raise HTTPException(status_code=404, detail="id not found")
    
#UPDATE
@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):

    try:
        list_data[id] = todo
        return list_data[id]
    except:
        raise HTTPException(status_code=404, detail="Data Not Found")

#DELETE
@app.delete('/todo/{id}')
async def delete_todo(id: int):

    try:
        data = list_data[id]
        list_data.pop(id)
        return data
    
    except:
        raise HTTPException(status_code=404, detail="Data Not Found")