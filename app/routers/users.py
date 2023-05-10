from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from dependencies import get_db
from sql_app import schemas, crud
from admin import utils

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# test
@router.get("/", response_model=list[schemas.User])
async def read_users(current_user: Annotated[schemas.User, Depends(utils.get_current_user)], db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# prod
@router.post("/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.create_user(db, user)
    return user
    
@router.get("/current", response_model=schemas.User)
async def read_user(user: Annotated[schemas.User, Depends(utils.get_current_user)]):
    return user

