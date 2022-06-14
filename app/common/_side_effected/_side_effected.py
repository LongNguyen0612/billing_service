from abc import ABC, abstractmethod
from app.common.pluggable import Executable
from typing import List, Callable

from app.common.utils import CommitUtility


class SideEffected(ABC):
    @abstractmethod
    def add_side_effected(self, side_effected):
        pass


class SideEffectedAppended(ABC):
    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def reset(self, exception):
        pass


class SideEffectedService(SideEffected, Executable):
    def __init__(self,
                 debug: bool = False):
        self.__debug = debug
        self.__side_effected_on_commit_services = []
        self.__side_effected_appended: List[SideEffectedAppended] = []

    def execute(self, handled: Callable, *args, **kwargs):
        commit_utility = CommitUtility(self.__side_effected_on_commit_services)
        try:
            result = handled(*args, **kwargs)
            commit_utility.before_commit()

            for _service in self.__side_effected_appended:
                _service.commit()

            commit_utility.after_commit()
            return result

        except Exception as exception:
            commit_utility.reset()

            for _service in self.__side_effected_appended:
                _service.reset(exception=exception)

            self.__side_effected_appended = []
            self.__side_effected_on_commit_services = []
            raise exception

    def add_side_effected(self, side_effected):
        if isinstance(side_effected, SideEffectedAppended):
            self.__side_effected_appended.append(side_effected)
            return

        self.__side_effected_on_commit_services.append(side_effected)