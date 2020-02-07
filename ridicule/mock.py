import inspect

from .mock_function import MockFunction
from .mock_object import MockObject


def Mock(obj):
    if inspect.isfunction(obj):
        return MockFunction(obj)
    return MockObject(obj)
