import sys

import pytest

from clime import clime
from docs_src.strings.tutorial_001 import main, Dude


def test_help(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("-h")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert 'positional arguments:\n  name' in captured.out
    """
    should look like this:
    usage: tutorial_001.py [-h] name

    positional arguments:
      name
    
    optional arguments:
      -h, --help  show this help message and exit
    """

def test_no_args(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "error: the following arguments are required: name" in captured.err


def test_no_flags_do_not_work_for_positional_args(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.extend(["--name", "joe"])
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "error: unrecognized arguments: --name" in captured.err


def test_args_inputted_properly(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("joe")
    main()
    captured = capsys.readouterr()
    assert captured.out == "hi! my name is joe\n"


def test_cli_input_equals_pure_input():
    from_cli = clime(Dude, args=["joe"])
    from_python = Dude(name="joe")
    assert from_cli == from_python
