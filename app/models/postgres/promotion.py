from sqlalchemy.orm import relationship, backref

from app.models.postgres._base_model import BaseModel
from sqlalchemy import (Column, String, ForeignKey, DECIMAL, Integer)

from app.utils.constant import UUID4_LENGTH, DECIMAL_PRECISION, DECIMAL_SCALE


class Promotion(BaseModel):
    __tablename__ = 'promotions'

    plan_id = Column(String(UUID4_LENGTH), ForeignKey('plans.id'), index=True)
    from_quantity = Column(Integer())
    to_quantity = Column(Integer())
    value = Column(String())
    promotion_type = Column(String())

    plan = relationship('Plan',
                        backref=backref('promotions'))
