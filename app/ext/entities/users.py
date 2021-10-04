"""
Representação da tabela de Users
"""

from sqlalchemy import Column, String, Integer
from app.ext.config import base

class Users(base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=true)
    name = Column(String)

    def __repr__(self):
        return f"Users [name={self.name}]"
