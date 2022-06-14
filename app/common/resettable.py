from abc import (ABC, abstractmethod)


class Resettable(ABC):

    @abstractmethod
    def reset(self, **kwargs):
        pass
