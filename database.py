from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://{mod}:{py@100}@localhost/{mehul}",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
