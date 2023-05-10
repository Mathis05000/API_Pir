from sqlalchemy.orm import Session
from admin.utils import get_password_hash

from . import models, schemas


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_message(db: Session, message: schemas.MessageCreate, user: schemas.User):
    db_message = models.Message(content=message.content, date=message.date, owner_id=user.id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message