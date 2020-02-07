from ridicule.exceptions import InvalidCall
from .base import MockBase
from .utils import is_valid_call


class MockFunction(MockBase):
    def __init__(self, function_):
        self._function = function_
        super().__init__()

    def __call__(self, *args, **kwargs):
        if not is_valid_call(self._function, args, kwargs):
            raise InvalidCall(self._function, args, kwargs)
        return self._mock(*args, **kwargs)
