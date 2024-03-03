from fastapi import APIRouter, Depends
from schemas import UserInputModel, UserOutputModel
from sqlalchemy.orm import Session
from database.db import get_db

from res.user import create_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)


# create new user
@router.post(
    '/create',
    response_model=UserOutputModel,
    status_code=201
)
async def create(request: UserInputModel, db: Session = Depends(get_db)):
    return create_user(db, request)