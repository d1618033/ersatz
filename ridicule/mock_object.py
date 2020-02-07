import inspect

from .base import MockBase
from .mock_function import MockFunction


_NOTSET = object()


class MockObject(MockBase):
    def __init__(self, obj):
        self.__obj = obj
        self.__cache = {}
        super().__init__()

    def __getattr__(self, item):
        attr = self.__cache.get(item, _NOTSET)
        if attr is _NOTSET:
            attr = self.__cache[item] = MockFunction(getattr(self.__obj, item))
        return attr

