from app.models.postgres._base_model import BaseModel
from sqlalchemy import (Column, String, ForeignKey, DECIMAL, Text)
from sqlalchemy.orm import (
    relationship, backref)
from app.models.utils import DECIMAL_PRECISION
from app.utils import UUID4_LENGTH, STRING_SIZE


class Price(BaseModel):
    __tablename__ = 'prices'

    value = Column(String(STRING_SIZE), nullable=False, unique=True, index=True)

