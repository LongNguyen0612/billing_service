from sqlalchemy.orm import relationship, backref

from app.models.utils.constant import UUID4_LENGTH
from app.models.postgres._base_model import BaseModel
from sqlalchemy import Column, String, Text, ForeignKey

from app.utils import STRING_SIZE


class Plan(BaseModel):
    __tablename__ = 'plans'
    price_id = Column(String(UUID4_LENGTH), ForeignKey('prices.id'), index=True)

    plan_name = Column(String(STRING_SIZE), nullable=False, unique=True, index=True)
    description = Column(Text())

    price = relationship('Price', backref='plans', uselist=False)

