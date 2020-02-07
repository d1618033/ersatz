import pytest
from unittest.mock import call
import ridicule
from ridicule.exceptions import InvalidCall


def test_two_args():
    def f(x, y):
        pass

    mock_f = ridicule.MockFunction(f)
    with pytest.raises(InvalidCall):
        mock_f()
    with pytest.raises(InvalidCall):
        mock_f(1)
    with pytest.raises(InvalidCall):
        mock_f(1, 2, 3)
    with pytest.raises(InvalidCall):
        mock_f(x=1, z=5)
    with pytest.raises(InvalidCall):
        mock_f(1, x=1)
    mock_f(1, 2)
    mock_f(x=1, y=2)
    mock_f(y=10, x=5)
    assert mock_f.call_args_list == [call(1, 2), call(x=1, y=2), call(x=5, y=10)]


def test_kwargs():
    def f(x, y, **kwargs):
        pass

    mock_f = ridicule.MockFunction(f)
    with pytest.raises(InvalidCall):
        mock_f(1, 2, 3)
    with pytest.raises(InvalidCall):
        mock_f(x=1, z=5)
    with pytest.raises(InvalidCall):
        mock_f(1, x=1)
    mock_f(1, 2, z=5)
    assert mock_f.call_args_list == [call(1, 2, z=5)]


def test_return_value():
    def f():
        pass

    mock_f = ridicule.MockFunction(f)
    mock_f.return_value = 10
    assert mock_f() == 10


def test_side_effect_list():
    def f():
        pass

    mock_f = ridicule.MockFunction(f)
    mock_f.side_effect = [1, 2, 3]
    assert mock_f() == 1
    assert mock_f() == 2
    assert mock_f() == 3


def test_side_effect_exception():
    def f():
        pass

    mock_f = ridicule.MockFunction(f)
    mock_f.side_effect = RuntimeError("e")
    with pytest.raises(RuntimeError):
        mock_f()
