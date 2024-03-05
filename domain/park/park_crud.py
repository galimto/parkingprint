from datetime import datetime

from sqlalchemy.orm import Session

from domain.park.park_schema import ParkCreate
from models import ParkInfo


def create_park(db: Session, park: ParkCreate):
    parkData = ParkInfo(
        title=park.title,
        memo=park.memo,
        create_date=datetime.now(),
        enter_date=park.enter_date,
    )
    db.add(parkData)
    db.commit()


def get_park_list(db: Session):
    park_list = db.query(ParkInfo).all()
    return park_list
