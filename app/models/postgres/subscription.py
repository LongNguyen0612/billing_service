from sqlalchemy.orm import relationship

from app.models.utils import UUID4_LENGTH
from app.models.postgres._base_model import BaseModel
from sqlalchemy import (Column, String, DateTime, ForeignKey, Float, Integer, null)
from sqlalchemy.orm import backref
from app.utils.constant import STRING_SIZE


class Subscription(BaseModel):
    __tablename__ = 'subscriptions'

    plan_id = Column(String(UUID4_LENGTH), ForeignKey('plans.id'), index=True)
    price_id = Column(String(UUID4_LENGTH), ForeignKey('prices.id'), index=True)
    promotion_id = Column(String(UUID4_LENGTH), ForeignKey('promotions.id'), index=True)

    start_time = Column(DateTime)
    end_time = Column(DateTime)
    month = Column(Integer())
    account_id = Column(String(UUID4_LENGTH))
    status = Column(String())
    order_id = Column(String(UUID4_LENGTH))

    plan = relationship('Plan', backref='subscriptions')
    price = relationship('Price', backref='subscriptions')
    promotion = relationship('Promotion', backref='subscriptions')

