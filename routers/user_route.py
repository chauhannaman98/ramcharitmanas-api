from fastapi import APIRouter, Depends, status
from schemas import UserInputModel, UserOutputModel, UserUpdateModel
from sqlalchemy.orm import Session
from database.db import get_db

from res.user import create_user, update_user, delete_user


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


# update user details
@router.put(
    '/update',
    response_model=UserOutputModel,
    status_code=status.HTTP_201_CREATED
)
async def update(request: UserUpdateModel, db: Session = Depends(get_db)):
    return update_user(db, request)


# delete user details
@router.delete(
    '/delete/{username}',
    status_code=status.HTTP_200_OK
)
async def delete(username: str, db: Session = Depends(get_db)):
    return delete_user(db, username)