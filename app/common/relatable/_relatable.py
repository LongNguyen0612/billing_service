from abc import (ABC, abstractmethod)

from sqlalchemy.orm import Session


class Relatable(ABC):
    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def flush(self):
        pass

    @abstractmethod
    def get_session(self) -> Session:
        pass
