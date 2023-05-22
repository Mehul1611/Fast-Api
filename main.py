from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()

class Book(BaseModel): #serializer
    title:str
    content:str
    author:str
    comment:bool

    class Config:
        orm_mode=True


db=SessionLocal()

@app.get('/Book',response_model=List[Book],status_code=200)
def get_all_books():
    books=db.query(models.Book).all()

    return books

@app.get('/book/{book_title}',response_model=Book,status_code=status.HTTP_200_OK)
def get_an_book(book_title:str):
    book=db.query(models.Book).filter(models.Book.title==book_title).first()
    return book

@app.post('/books',response_model=Book,
        status_code=status.HTTP_201_CREATED)
def create_an_book(book:Book):
    db_book=db.query(models.Book).filter(models.Book.author==book.author).first()

    if db_book is not None:
        raise HTTPException(status_code=400,detail="Book already exists")



    new_book=models.Book(
        title=book.title,
        author=book.author,
        content=book.content,
        comment=book.comment
    )


    

    db.add(new_book)
    db.commit()

    return new_book

@app.put('/book/{book_title}',response_model=Book,status_code=status.HTTP_200_OK)
def update_an_book(book_title:str,book:Book):
    book_to_update=db.query(models.Book).filter(models.Book.title==book_title).first()
    book_to_update.author=book.author
    book_to_update.content=book.content
    book_to_update.comment=book.comment

    db.commit()

    return book_to_update

@app.delete('/book/{book_title}')
def delete_book(book_title:str):
    book_to_delete=db.query(models.Book).filter(models.Book.title==book_title).first()

    if book_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(book_to_delete)
    db.commit()

    return book_to_delete
