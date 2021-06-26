import sys

import pytest


@pytest.fixture()
def set_cli_sys_argv():
    """
    Clime commands are dependent on a a sys.argv similar to what a python program would get from the command line.
    Pytest and other tools modify the sys.argv
    This fixture temporarily change the value so tests will work as expected.
    :return:
    """
    current_sys_arv = sys.argv
    sys.argv = current_sys_arv[:1]
    try:
        yield
    finally:
        sys.argv = current_sys_arv