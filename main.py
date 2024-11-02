from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get(path="/sheep/{id}", response_model=Sheep)
@app.post(path="/sheep/{id}", response_model=Sheep, status_code=status.HTTP_201_CREATED)

def add_sheep(sheep: Sheep) -> Sheep:
    if sheep.id in db.data:
        raise ValueError(status_code=400, detail="Id exsist")
    db.data[sheep.id] = sheep
    return sheep

def read_sheep(id: int):
    return db.get_sheep(id)