import sys

import pytest

from docs_src.usage.tutorial_001 import main


def test_help(set_cli_sys_argv, capsys):
    sys.argv.append("-h")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "Amaze your friends by printing you name to the console" in captured.out
    # should look like this:
    """
    usage:
        Amaze your friends by printing you name to the console

    positional arguments:
      name        type: <str>
    
    optional arguments:
      -h, --help  show this help message and exit

    """
