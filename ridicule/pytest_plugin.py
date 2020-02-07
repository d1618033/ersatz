import pytest
from .patch import GorillaPatch


@pytest.fixture
def gpatch():
    patch = GorillaPatch()
    yield patch
    patch.undo()
