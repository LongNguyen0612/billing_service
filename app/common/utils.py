"""
Common classes support generic interfaces behavior
"""
from typing import List

from app.common.after_commit import AfterCommit, BeforeCommit
from app.common.resettable import Resettable


class CommitUtility(BeforeCommit, AfterCommit, Resettable):
    """
    Utils class support trigger BeforeCommit, AfterCommit, Resettable subclasses
    """

    def __init__(self, side_effected_items: List):
        self.__side_effected_items = side_effected_items

    def reset(self):
        for service in reversed(self.__side_effected_items):
            if not isinstance(service, Resettable):
                continue

            service.reset()

    def after_commit(self, *args, **kwargs):
        for service in self.__side_effected_items:
            if not isinstance(service, AfterCommit):
                continue

            service.after_commit()

    def before_commit(self, *args, **kwargs):
        for service in self.__side_effected_items:
            if not isinstance(service, BeforeCommit):
                continue

            service.before_commit()
