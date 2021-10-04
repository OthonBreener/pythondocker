"""
Representação da tabela de Users
"""

from sqlalchemy import Column, String, Integer
from app.ext.config.base import base

class Users(base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Users [name={self.name}]"
