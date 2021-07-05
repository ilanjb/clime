import sys

import pytest

from clime import clime
from docs_src.integers_floats_and_other_simple_classes.tutorial_002 import main, Dude


def test_help(set_cli_sys_argv, capsys):

    sys.argv.append("-h")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert (
        "positional arguments" not in captured.out
    )
    assert "--age-in-years" in captured.out
    # should look like this
    """
    usage: tutorial_002.py [-h] [--age-in-years AGE_IN_YEARS]
    
    optional arguments:
      -h, --help            show this help message and exit
      --age-in-years AGE_IN_YEARS
                            type: <int> (default: None)
    """


def test_nothing_inputed(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    main()
    captured = capsys.readouterr()
    assert captured.out == "A script never reveals its age\n"

def test_correct_input(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.extend(['--age-in-years', '12'])
    main()
    captured = capsys.readouterr()
    assert captured.out == "I am 12 years old.\n"

def test_cli_input_equals_pure_input():
    from_cli = clime(Dude, args=["1"])
    from_python = Dude(1)
    assert from_cli == from_python
