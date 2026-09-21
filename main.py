from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()

book:str = ""

class BookAdd(BaseModel):
    title: str

@app.get("/book", response_model= str)
def get_book():
    return f'Любимая книга: {book}'

@app.post("/book", response_model= str, status_code=status.HTTP_201_CREATED)
def create_book(name: BookAdd):
    global book
    book = name.title
    return book