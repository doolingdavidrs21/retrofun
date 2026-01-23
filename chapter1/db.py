import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):
    pass



load_dotenv()

# print('Database URL:', os.environ['DATABASE_URL'])

engine = create_engine(os.environ["DATABASE_URL"])


