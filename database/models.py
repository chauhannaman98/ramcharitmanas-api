from database.db import Base
from sqlalchemy import Column, UnicodeText
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


class ManasChapter(Base):
    __tablename__ = 'manas_chapter'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(UnicodeText)
    name_transliterated = Column(UnicodeText)
    name_translated = Column(UnicodeText)
    # verses_count = Column(Integer)
    chapter_number = Column(Integer)
    name_meaning = Column(UnicodeText)
    chapter_summary = Column(UnicodeText)
    chapter_summary_hindi = Column(UnicodeText)