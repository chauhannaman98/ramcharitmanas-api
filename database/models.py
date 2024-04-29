from database.db import Base
from sqlalchemy import Column, UnicodeText, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP, String
from sqlalchemy.orm import relationship


class ManasTranslation(Base):
    __tablename__ = 'manas_translations'

    id = Column(Integer, primary_key=True, autoincrement=True,)
    verse_id = Column(Integer, ForeignKey("manas_verses.id"))
    language = Column(String(255))
    translation = Column(UnicodeText)


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


class ManasVerse(Base):
    __tablename__ = 'manas_verses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    verse_number = Column(Integer)
    chapter_number = Column(Integer, ForeignKey("manas_chapter.id"))
    verse_type = Column(UnicodeText)
    verse_text = Column(UnicodeText)
    transliteration = Column(UnicodeText)

    # relationships
    # translations = relationship(ManasTranslation, backref='manas_verses', lazy='joined')