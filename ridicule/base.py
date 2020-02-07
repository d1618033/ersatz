import unittest.mock


class MockBase:
    def __init__(self):
        self._mock = unittest.mock.Mock()

    def __getattr__(self, k):
        return getattr(self._mock, k)

    def __setattr__(self, key, value):
        if key in ["return_value", "side_effect"]:
            setattr(self._mock, key, value)
        else:
            self.__dict__[key] = value
