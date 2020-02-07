import pytest

from ridicule.exceptions import InvalidCall
from ridicule.mock_object import MockObject


def test_simple():
    class Real:
        def method(self, y, z):
            pass

    mock = MockObject(Real())
    with pytest.raises(InvalidCall):
        mock.method()
    with pytest.raises(InvalidCall):
        mock.method(1, 2, 3)
    with pytest.raises(InvalidCall):
        mock.method(x=1, y=2)
    mock.method(y=5, z=10)
