from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    completed : bool

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None

class TaskResponse(TaskBase): 
    id: int