import logging
from abc import (ABC, abstractmethod)
from typing import List

from app.common.after_commit import (
    AfterCommit,
    BeforeCommit)


logger = logging.getLogger(__name__)


class GeneratedException(Exception):
    pass


class Generated(ABC):
    @abstractmethod
    def generate(self):
        pass


class GeneratedResultSettable(ABC):

    @abstractmethod
    def set_result(self, result):
        pass


class GeneratedAppendable(ABC):

    @abstractmethod
    def append_generated(self, generated: Generated, index: int = None):
        pass


class SettableGenerated(Generated, GeneratedResultSettable, ABC):
    pass


class Generator(SettableGenerated, GeneratedAppendable, AfterCommit, BeforeCommit):
    """
    Run-time code modification generator.
    """

    def __init__(self,
                 generators: List[SettableGenerated] = None,
                 current_result=None):

        self.__current_result = current_result
        self.__generators = generators or []

    def append_generated(self, generator: SettableGenerated, index: int = None):
        if isinstance(index, int):
            self.__generators.insert(index, generator)
            return

        self.__generators.append(generator)

    def set_result(self, result):
        self.__current_result = result

    def generate(self):
        result = self.__current_result

        for generator in self.__generators:
            generator.set_result(result)
            result = generator.generate()

        return result

    def after_commit(self, *args, **kwargs):
        for generator in self.__generators:
            if isinstance(generator, AfterCommit):
                generator.after_commit()

    def before_commit(self, *args, **kwargs):
        for generator in self.__generators:
            if isinstance(generator, BeforeCommit):
                generator.before_commit()
