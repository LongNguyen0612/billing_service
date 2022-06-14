import datetime
from datetime import date

from dateutil.relativedelta import relativedelta


def get_today(today: datetime = None):
    if not today:
        today = date.today()

    return today


def get_after_month(after_month: datetime = None):
    if not after_month:
        after_month = date.today() + relativedelta(months=+1)

    return after_month
