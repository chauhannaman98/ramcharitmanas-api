from pydantic import BaseModel
from typing import List


class ChapterModel(BaseModel):
    id: int
    name: str
    name_transliterated: str
    name_translated: str
    chapter_number: int
    name_meaning: str
    chapter_summary: str
    chapter_summary_hindi: str


class VerseTranslationModel(BaseModel):
    id: int
    language: str
    translation: str


class VerseTranslationOutputModel(BaseModel):
    data: List[VerseTranslationModel]


class VerseModel(BaseModel):
    id: int
    verse_number: int
    chapter_number: int
    verse_type: str
    verse_text: str
    transliteration : str
    # translations: List[VerseTranslationModel]
    class Config():
        from_attributes = True


class VerseOutputModel(BaseModel):
    data: List[VerseModel]