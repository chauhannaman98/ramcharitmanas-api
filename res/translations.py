from sqlalchemy.orm import Session
from database.models import ManasTranslation
from fastapi import HTTPException, status


def get_all_translations(db: Session):
    translations = db.query(ManasTranslation
        ).order_by(
            ManasTranslation.id.asc()
        ).all()
    
    print(translations)
    
    return translations


def get_translation_by_verse(db: Session, verse_number: int):
    translation = db.query(ManasTranslation).filter(
        ManasTranslation.verse_id == verse_number
    ).all()

    if translation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Chapter number {str(verse_number)} does not exist"
        )
    
    return translation