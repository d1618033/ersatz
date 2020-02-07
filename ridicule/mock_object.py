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
        mocked_attr = self.__cache.get(item, _NOTSET)
        if mocked_attr is _NOTSET:
            attr = getattr(self.__obj, item)
            if inspect.ismethod(attr):
                mocked_attr = MockFunction(attr)
            else:
                mocked_attr = attr
        return mocked_attr

