import sys

import pytest

from clime import clime
from docs_src.integers_floats_and_other_simple_classes.tutorial_001 import main, Dude


def test_help(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("-h")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert (
        "positional arguments:\n  age_in_years  type: <int>" in captured.out
    )  # note that default arguments keep there underscores
    # should look like this:
    """
    usage: tutorial_001.py [-h] age_in_years
    
    positional arguments:
      age_in_years  type: <int>
    
    optional arguments:
      -h, --help    show this help message and exit

    """


def test_args_inputted_properly(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("7")
    main()
    captured = capsys.readouterr()
    assert captured.out == "I am 7 years old.\n"


def test_cli_input_equals_pure_input():
    from_cli = clime(Dude, args=["1"])
    from_python = Dude(1)
    assert from_cli == from_python
