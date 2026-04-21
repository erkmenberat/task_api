#main.py

from fastapi import FastAPI#, Depends #HTTPException, 
# from typing import List, Optional
# from uuid import UUID, uuid4 
#from app.database import get_db
#from sqlalchemy.orm import Session 
# from app.schemas.schema import TaskResponse
# from app.models.models import Task

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# @app.get("/health")
# def health_check(db: Session = Depends(get_db)):
#     try:
#         from sqlalchemy import text
#         db.execute(text("SELECT 1"))
#         return {"status": "ok", "database": "connected"}
#     except Exception as e:
#         return {"status": "error", "database": str(e)}