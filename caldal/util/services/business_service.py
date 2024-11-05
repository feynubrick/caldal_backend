from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from ninja import Schema

ReturnType = TypeVar("ReturnType")
InputType = TypeVar("InputType", bound=Schema)


class BusinessService(Generic[InputType, ReturnType], ABC):
    def run(self, data: InputType):
        self._before_run(data)
        return_val = self._run(data)
        self._after_run(data, return_val)
        return return_val

    def _before_run(self, data: InputType):
        pass

    def _after_run(self, data: InputType, return_val: ReturnType):
        pass

    @abstractmethod
    def _run(self, data: InputType) -> ReturnType:
        pass
