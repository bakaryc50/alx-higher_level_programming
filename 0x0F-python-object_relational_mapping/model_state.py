#!/usr/bin/python3
"""
Script that contains the class definition of a State and an instance Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    State class definition
    Attributes:
        id: the identifier of the class
        name: the class name
    """
    __tablename__ = "states"

    id = Column(
            Integer,
            nullable=False,
            autoincrement=True,
            unique=True,
            primary_key=True)
    name = Column(String(128), nullable=False)
