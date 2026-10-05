from fastapi import FastAPI,status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Category(BaseModel):
    id: str
    name: str

class CategoryCreate(BaseModel):
    name: str

class CategoryUpdate(BaseModel):
    name: str


categories: list[Category] = []

@app.get("/categories")
def get_categories() -> list[Category]:
    return categories

@app.post("/categories", status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate):
    new_category = Category(id=str(uuid4()),name=payload.name)
    categories.append(new_category)
    return new_category

@app.patch("/categories/{category_id}", status_code=status.HTTP_200_OK)
def update_category(category_id: str, payload: CategoryUpdate):
    for category in categories:
        if category.id == category_id:
            category.name = payload.name
            return category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

@app.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: str):
    for category in categories:
        if category.id == category_id:
            categories.remove(category)
            return category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
