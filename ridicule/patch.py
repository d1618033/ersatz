import inspect
from contextlib import contextmanager

from _pytest.monkeypatch import MonkeyPatch, notset, derive_importpath

from ridicule import Mock


class GorillaPatch:
    def __init__(self):
        self._monkeypatch = MonkeyPatch()

    @contextmanager
    def context(self):
        m = GorillaPatch()
        try:
            yield m
        finally:
            m.undo()

    def _get_old_val(self, target, name=notset):
        __tracebackhide__ = True

        if name is notset:
            assert isinstance(target, str)
            name, target = derive_importpath(target, True)

        if not hasattr(target, name):
            raise AttributeError(name)
        oldval = getattr(target, name, notset)
        # Avoid class descriptors like staticmethod/classmethod.
        if inspect.isclass(target):
            oldval = target.__dict__.get(name, notset)
        return oldval

    def mock(self, target, name=notset):
        mock = Mock(self._get_old_val(target, name))
        self._monkeypatch.setattr(target, name, mock)
        return mock

    def __getattr__(self, item):
        return getattr(self._monkeypatch, item)
