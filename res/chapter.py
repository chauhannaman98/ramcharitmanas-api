from sqlalchemy.orm import Session, joinedload
from schemas import ChapterModel, VerseModel
from database.models import ManasChapter, ManasVerse
from fastapi import HTTPException, status, Response
from typing import List



# method returns a list of all the chapters
def get_all_chapters(db: Session) -> List:
    chapters = db.query(ManasChapter).order_by(
        ManasChapter.chapter_number.asc()
    ).all()

    return chapters


# method return a chapter
def get_chapter(db: Session, chapter_number: int) -> ChapterModel:
    chapter = db.query(ManasChapter).filter(ManasChapter.chapter_number == chapter_number).first()

    if chapter is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter number {str(chapter_number)} does not exist"
        )
    
    return chapter


# method returns a list of verses in a chapter
def get_all_verses(db: Session, chapter_number: int):
    verses = db.query(ManasVerse).filter(
        ManasVerse.chapter_number == chapter_number
    ).order_by(
        ManasVerse.verse_number.asc()
    ).all()

    if verses:
        return verses
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No data found for chapter {str(chapter_number)}."
    )


# returns the particular verse from the chapter
def get_verse_from_chapter(db: Session, chapter_num: int, verse_num: int) -> VerseModel:
    verse = db.query(ManasVerse).filter(
        ManasVerse.chapter_number == chapter_num,
        ManasVerse.verse_number == verse_num
    ).first()

    if verse:
        return verse
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No verse number {verse_num} found in chapter {chapter_num}"
    )