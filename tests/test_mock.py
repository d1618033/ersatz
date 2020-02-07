from ridicule import Mock, MockFunction, MockObject


def test_function():
    def f():
        pass
    assert isinstance(Mock(f), MockFunction)


def test_object():
    class MyClass:
        pass
    assert isinstance(Mock(MyClass()), MockObject)
