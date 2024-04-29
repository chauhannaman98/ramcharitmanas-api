from fastapi import APIRouter, Depends, status
from requests import get
from schemas import ChapterModel, VerseModel, VerseOutputModel
from database.db import get_db
from sqlalchemy.orm import Session
from res import chapter
from typing import List



router = APIRouter(
    prefix='/chapters',
)


@router.get(
    '/',
    response_model=List[ChapterModel],
    status_code=status.HTTP_200_OK,
    tags=['chapters']
)
def get_all_chapters(db: Session = Depends(get_db)):
    return chapter.get_all_chapters(db)


@router.get(
    '/{chapter_num}',
    response_model=ChapterModel,
    status_code=status.HTTP_200_OK,
    tags=['chapters']
)
async def get_chapter(chapter_num: int, db: Session = Depends(get_db)):
    return chapter.get_chapter(db, chapter_num)


@router.get(
    '/{chapter_num}/verses',
    status_code=status.HTTP_200_OK,
    # response_model=List[VerseModel],
    tags=['verses']
)
async def get_all_verses_by_chapter(chapter_num: int, db: Session = Depends(get_db)):
    return chapter.get_all_verses(db, chapter_num)


@router.get(
    '/{chapter_num}/verses/{verse_num}',
    status_code=status.HTTP_200_OK,
    response_model=VerseModel,
    tags=['verses']
)
async def get_particular_verse_from_chapter(chapter_num: int, verse_num: int, db: Session = Depends(get_db)):
    return chapter.get_verse_from_chapter(db, chapter_num, verse_num)