from sqlalchemy import Column, Integer, DateTime, VARCHAR

from flaskapi.helpers.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(25))
    surname = Column(VARCHAR(25))
    added = Column(DateTime)
    edited = Column(DateTime)

    def __init__(self, first_name=None, surname=None, added=None, edited=None):
        self.first_name = first_name
        self.surname = surname
        self.added = added
        self.edited = edited

    def __repr__(self):
        return {'id': self.id}

