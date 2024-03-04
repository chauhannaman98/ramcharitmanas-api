from sqlalchemy.orm import Session
from schemas import ChapterModel
from database.models import ManasChapter
from fastapi import HTTPException, status
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