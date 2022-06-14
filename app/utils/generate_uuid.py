from sqlalchemy.sql import expression
from sqlalchemy import DateTime
import uuid


class utcnow(expression.FunctionElement):
    type = DateTime()


def generate_uuid():
    return str(uuid.uuid4())
