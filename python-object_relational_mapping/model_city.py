#!/usr/bin/python3
"""class City
"""


from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy import Sequence
from model_state import Base


class City(Base):
    """city class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)    
    name = Column(String(255), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
