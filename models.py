from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class Book(Base):
    __tablename__='books'
    title=Column(Integer,primary_key=True)
    author=Column(String(255),nullable=False,unique=True)
    content=Column(Text)

    comment=Column(Boolean,default=False)


    def __repr__(self):
        return f"<Book name={self.name} price={self.price}>"
