from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from dependencies import get_db
from sql_app import schemas, crud
from admin import utils
from analyse.message_analyses import message_analyses

router = APIRouter(
    prefix="/messages",
    tags=["messages"]
)


@router.get("/", response_model=list[schemas.Message])
async def get_messages(
    current_user: Annotated[schemas.User, Depends(utils.get_current_user)], 
    db: Session = Depends(get_db)
    ):
    return current_user.messages

@router.post("/", response_model=schemas.Message)
async def add_messages(
        message: schemas.MessageCreate, 
        current_user: Annotated[schemas.User, Depends(utils.get_current_user)], 
        db: Session = Depends(get_db)
    ):
    message = crud.create_message(db, message, current_user)
    message_analyses(message)
    return message
