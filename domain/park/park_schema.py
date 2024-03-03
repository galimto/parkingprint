from datetime import datetime

from pydantic import BaseModel


class ParkCreate(BaseModel):

    title: str
    memo: str

    enter_date: datetime
