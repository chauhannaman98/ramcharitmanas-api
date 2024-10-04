from sqlalchemy.orm import Session, joinedload
from schemas import ChapterModel, VerseModel
from database.models import ManasChapter, ManasVerse
from fastapi import HTTPException, status, Response
from typing import List
import json
import ast
from res.row2dict import row2dict
import redis
from dotenv import load_dotenv
import os


load_dotenv()

rd = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    password=os.getenv('REDIS_PASSWORD')
    )

try:
    rd.ping()  # Test connection
    print("Connected to Redis!")
except redis.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")

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
    redis_key = f"chapter_{chapter_number}"
    cached_data = rd.get(redis_key)

    if cached_data:
        cached_data_str = cached_data.decode('utf-8')
        cached_data_list = ast.literal_eval(cached_data_str)
        return cached_data_list
    else:
        verses = db.query(ManasVerse).filter(
            ManasVerse.chapter_number == chapter_number
        ).order_by(
            ManasVerse.verse_number.asc()
        ).all()

        if verses:
            parsed_list = []
            for verse in verses:
                parsed_list.append(row2dict(verse))

            rd.set(redis_key, str(parsed_list))
            rd.expire(redis_key, os.getenv('REDIS_CHAPTER_CACHE_TIMEOUT'))
            return parsed_list
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No data found for chapter {str(chapter_number)}."
        )


# returns the particular verse from the chapter
def get_verse_from_chapter(db: Session, chapter_num: int, verse_num: int) -> VerseModel:
    print("### calling get_verse_from_chapter ###")
    verse = db.query(ManasVerse).filter(
        ManasVerse.chapter_number == chapter_num,
        ManasVerse.verse_number == verse_num
    ).first()
    
    print(verse)

    if verse:
        return verse
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No verse number {verse_num} found in chapter {chapter_num}"
    )