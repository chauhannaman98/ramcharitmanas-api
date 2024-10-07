from sqlalchemy.orm import Session, joinedload
from schemas import ChapterModel, VerseModel
from database.models import ManasChapter, ManasVerse
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
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
    # print("Connected to Redis!")
except redis.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")


# method returns a list of all the chapters
def get_all_chapters(db: Session) -> List:
    try:
        chapters = db.query(ManasChapter).order_by(
            ManasChapter.chapter_number.asc()
        ).all()
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve data from database."
        )
    
    response = {
        "status": "true",
        "data": chapters
    }
    json_str = jsonable_encoder(response)
    return JSONResponse(content=json_str)


# method return a chapter
def get_chapter(db: Session, chapter_number: int) -> ChapterModel:
    try:
        chapter = db.query(ManasChapter).filter(
            ManasChapter.chapter_number == chapter_number
            ).first()
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve data from database."
        )

    if chapter:
        response = {
            "status": "true",
            "data": chapter
        }
        json_str = jsonable_encoder(response)
        return JSONResponse(content=json_str)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Chapter number {str(chapter_number)} does not exist"
    )


# method returns a list of verses in a chapter
def get_all_verses(db: Session, chapter_number: int):
    redis_key = f"chapter_{chapter_number}"

    try:
        cached_data = rd.get(redis_key)
    except:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve key {str(redis_key)} from cache."
        )

    if cached_data:
        cached_data_str = cached_data.decode('utf-8')
        cached_data_list = ast.literal_eval(cached_data_str)
        response = {
            "status": "true",
            "data": cached_data_list
        }
        json_str = jsonable_encoder(response)
        return JSONResponse(content=json_str)
    else:
        try:
            verses = db.query(ManasVerse).filter(
                ManasVerse.chapter_number == chapter_number
            ).order_by(
                ManasVerse.verse_number.asc()
            ).options(
                joinedload(ManasVerse.translations)
            ).all()
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to retrieve data from database."
            )

        if verses:
            parsed_list = []
            for verse in verses:
                parsed_list.append(row2dict(verse))

            try:
                rd.set(redis_key, str(parsed_list))
                rd.expire(redis_key, os.getenv('REDIS_CHAPTER_CACHE_TIMEOUT'))
            except:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Failed to set data to redis cache with key: {str(redis_key)}."
                )
            response = {
                "status": "true",
                "data": parsed_list
            }
            json_str = jsonable_encoder(response)
            return JSONResponse(content=json_str)
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No data found for chapter {str(chapter_number)}."
        )


# returns the particular verse from the chapter
def get_verse_from_chapter(db: Session, chapter_num: int, verse_num: int) -> VerseModel:
    try:
        verse = db.query(ManasVerse).filter(
            ManasVerse.chapter_number == chapter_num,
            ManasVerse.verse_number == verse_num
        ).first()
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve data from database."
        )

    if verse:
        response = {
            "status": "true",
            "data": verse
        }
        json_str = jsonable_encoder(response)
        return JSONResponse(content=json_str)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No verse number {verse_num} found in chapter {chapter_num}"
    )