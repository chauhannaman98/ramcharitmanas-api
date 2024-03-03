from fastapi import APIRouter, Depends, status
from requests import get
from schemas import ChapterModel, AllChapterOutputModel
from database.db import get_db
from sqlalchemy.orm import Session
from res import chapter
from typing import List



router = APIRouter(
    prefix='/chapters',
    tags=['chapters']
)


@router.get(
    '/',
    response_model=List[ChapterModel],
    status_code=status.HTTP_200_OK
)
def get_all_chapters(db: Session = Depends(get_db)):
    return chapter.get_all_chapters(db)


@router.get(
    '/{chapter_num}',
    response_model=ChapterModel,
    status_code=status.HTTP_200_OK
)
async def get_chapter(chapter_num: int, db: Session = Depends(get_db)):
    return chapter.get_chapter(db, chapter_num)