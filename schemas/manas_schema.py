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