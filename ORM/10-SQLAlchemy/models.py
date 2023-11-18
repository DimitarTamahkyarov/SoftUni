from sqlalchemy import Text, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)


class Recipe(Base):

    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)

