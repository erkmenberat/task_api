from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4 

app = FastAPI(title = "amk")

class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks = [] # here i have to connect a DB - SQLAlchemy

@app.post("/tasks/{task_title}", response_model=Task)
async def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task 

#Routing to App Home /: 
@app.get("/")
async def root():
    return {"message": "This is a Todo API -- Usage --> // "}

#Lists the Tasks: 
@app.get("/tasks/", response_model=List[Task]) # why not /task why /task/
async def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task: Task):
    for t in tasks:
        if t.id == task.id: 
            return Task
    return {"message": "No Task found : 404"} 


