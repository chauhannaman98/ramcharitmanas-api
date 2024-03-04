from fastapi import FastAPI
from routers import user_route, chapter_route
from database import models
from database.db import engine



app = FastAPI()
app.include_router(chapter_route.router)
# app.include_router(user_route.router)


@app.get("/")
async def root():
    return {
        "message": "Jai Shree Ram!",
        "enpoints-available": {
            'chapter': [
                '/chapters',
                '/chapters/{chapter_number}',
                '/chapters/{chapter_number}/verses',
                '/chapters/{chapter_number}/verses/{verse_number}'
            ]
        }
    }


# create all tables
models.Base.metadata.create_all(engine)