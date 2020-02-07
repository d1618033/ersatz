import os
from unittest import mock

import pytest

from ridicule.exceptions import InvalidCall


def test_basic(gpatch):
    mock_popen = gpatch.mock(os, "popen")
    with pytest.raises(InvalidCall):
        os.popen("ls", mode_="w")
    os.popen("ls", mode="r")
    assert mock_popen.call_args_list == [
        mock.call("ls", mode="r")
    ]
