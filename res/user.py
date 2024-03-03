from schemas.user_schema import UserInputModel, UserOutputModel, UserUpdateModel
import datetime
from sqlalchemy.orm import Session
from database.models import DBUser
from fastapi import HTTPException, status
from res.hash import Hash



def create_user(db: Session, request: UserInputModel) -> UserOutputModel:
    db_username = db.query(DBUser).filter(DBUser.username == request.username).first()
    db_email = db.query(DBUser).filter(DBUser.email == request.email).first()
    if db_username or db_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail='Username or email already exists.'
        )
    
    new_user = DBUser(
        created_at = datetime.datetime.now(),
        username = request.username,
        first_name = request.first_name,
        last_name = request.last_name,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def update_user(db: Session, request: UserUpdateModel) -> UserOutputModel:
    db_user = db.query(DBUser).filter(DBUser.username == request.username).first()

    if db_user:
        if request.email:
            db_user.email = request.email
        if request.password:
            db_user.password = request.password
        if request.first_name:
            db_user.first_name = request.first_name
        if request.last_name:
            db_user.last_name = request.last_name
        if request.password:
            db_user.password = Hash.bcrypt(request.password)

        db.commit()
        db.refresh(db_user)

        return db_user
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Username {request.username} is not a valid user"
        )