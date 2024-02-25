from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base


class Question(Base):
    __tablename__ = "park"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    memo = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    enter_date = Column(DateTime, nullable=False)

    checkout_date = Column(DateTime, nullable=True)
