import email
from schemas.user_schema import UserInputModel, UserOutputModel
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