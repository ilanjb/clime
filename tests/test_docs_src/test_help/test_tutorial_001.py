import sys

import pytest

from docs_src.help.tutorial_001 import main


def test_help(set_cli_sys_argv, capsys):
    sys.argv.append("-h")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "name        Your first name" in captured.out
    # should look like this:
    """
    usage: tutorial_001.py [-h] name
    
    positional arguments:
      name        Your first name
    
    optional arguments:
      -h, --help  show this help message and exit
    """
