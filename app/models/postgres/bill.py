from sqlalchemy.orm import relationship, backref

from app.models.postgres._base_model import BaseModel
from sqlalchemy import (Column, String, DECIMAL, Integer, ForeignKey)

from app.utils.constant import DECIMAL_SCALE, STRING_SIZE, DECIMAL_PRECISION, UUID4_LENGTH


class Bill(BaseModel):
    __tablename__ = 'bills'

    subscription_id = Column(String(UUID4_LENGTH), ForeignKey('subscriptions.id'), index=True)

    total = Column(DECIMAL(precision=DECIMAL_PRECISION, scale=DECIMAL_SCALE, asdecimal=False), default=0.00)
    discount = Column(Integer, default=0)
    sub_total = Column(DECIMAL(precision=DECIMAL_PRECISION, scale=DECIMAL_SCALE, asdecimal=False), default=0.00)
    status = Column(String)

    subscription = relationship('Subscription',
                                backref=backref('bills', cascade="all, delete-orphan", passive_deletes=True),
                                uselist=False)


