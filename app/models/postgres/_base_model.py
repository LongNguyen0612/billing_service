import datetime
from typing import List, Dict

from sqlalchemy import (Column, String, DateTime, Boolean, inspect, MetaData)
from sqlalchemy.ext.declarative import declarative_base


from app.models.utils import UUID4_LENGTH
from app.constants import ISO_8601

from dateutil.parser import parse

from app.utils import generate_uuid

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    id = Column(String(UUID4_LENGTH), primary_key=True, default=generate_uuid)
    _created = Column(DateTime, default=datetime.datetime.utcnow().isoformat(), index=True)
    _updated = Column(DateTime, default=datetime.datetime.utcnow().isoformat())
    _deleted = Column(Boolean, server_default="false")

    def serialize(self) -> dict:
        serialized_model = dict()
        for column in inspect(self).mapper.column_attrs:
            column_value = getattr(self, column.key)
            if column_value and isinstance(column.columns[0].type, DateTime):
                column_value = parse(str(column_value)).strftime(ISO_8601)
            serialized_model[column.key] = column_value

        return serialized_model
