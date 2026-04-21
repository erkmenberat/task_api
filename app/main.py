#main.py

from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
from uuid import UUID, uuid4 
from database import get_db
from sqlalchemy.orm import Session 
from schemas.schema import TaskResponse
from models.models import Task


app = FastAPI(root_path="/api")


###
### --> issue -> /docs "not found"
###

    # @app.get("/tasks/", response_model=List[TaskResponse])
    # async def read_tasks(db: Session=Depends(get_db)):
    #     tasks = db.query(Task).all()
    #     return tasks

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}
    

# @app.post("/tasks/{task_title}", response_model=Task)
# async def create_task(task: Task):
#     task.id = uuid4()
#     tasks.append(task)
#     return task 

# #Routing to App Home /: 
# @app.get("/")
# async def root():
#     return {"message": "This is a Todo API -- Usage --> // "}

#Lists the Tasks: 


# @app.get("/tasks/{task_id}", response_model=Task)
# async def read_task(task: Task):
#     for t in tasks:
#         if t.id == task.id: 
#             return Task
#     return {"message": "No Task found : 404"} 


