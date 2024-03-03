from database.db import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP, String


class DBUser(Base):
    __tablename__ = 'users'

    id = id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP, nullable=True)
    username = Column(String, nullable=False)
    email = Column(String(255), nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    password = Column(String, nullable=False)