from abc import (ABC, abstractmethod)


class AfterCommit(ABC):
    @abstractmethod
    def after_commit(self, *args, **kwargs):
        pass


class BeforeCommit(ABC):
    @abstractmethod
    def before_commit(self, *args, **kwargs):
        pass
