from fastapi import APIRouter, status, Depends
from schemas import VerseTranslationOutputModel
from sqlalchemy.orm import Session
from database.db import get_db
from res.translations import get_translation_by_verse


router = APIRouter(
    prefix='/translations',
)

@router.get(
    '/verse/{verse_number}',
    status_code=status.HTTP_200_OK,
    # response_model=VerseTranslationOutputModel,
    tags=['translations']
)
def get_translation_by_verse_number(verse_number: int, db: Session = Depends(get_db)):
    return get_translation_by_verse(db, verse_number)