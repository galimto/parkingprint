from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from database import get_db
from models import ParkInfo
from domain.park import park_crud
from domain.park import park_schema

router = APIRouter(
    prefix="/api/park",
)


@router.get("/list")
def park_list(db: Session = Depends(get_db)):

    _park_list = park_crud.get_park_list(db)

    return _park_list


@router.post("create")
def park_create(_park_info: park_schema.ParkCreate, db: Session = Depends(get_db)):

    park_crud.create_park(db, _park_info)
