from fastapi import APIRouter

from database import SessionLocal
from models import ParkInfo
from domain.park import park_crud
from domain.park import park_schema

router = APIRouter(
    prefix="/api/park",
)


@router.get("/list")
def question_list():
    db = SessionLocal()
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    db.close()
    return


@router.post("create")
def park_create(_park_info: park_schema.ParkCreate):
    db = SessionLocal()
    park_crud.create_park(db, _park_info)
