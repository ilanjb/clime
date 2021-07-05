import sys

import pytest

from clime import clime
from docs_src.strings.tutorial_003 import main, Dude


def test_help(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("--help")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()

    assert "optional arguments:" in captured.out
    assert "--name NAME" in captured.out
    assert "(default: None)" in captured.out
    assert "positional arguments" not in captured.out
    """
    should like like this... 

    usage: _jb_pytest_runner.py [-h] [--name NAME]

    optional arguments:
    -h, --help   show this help message and exit
    --name NAME  (default: None)
    """


def test_good_with_default(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    main()
    captured = capsys.readouterr()
    assert "hi! my name is a secret" in captured.out


def test_good_with_argument(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.extend(["--name", "mike"])
    main()
    captured = capsys.readouterr()
    assert "hi! my name is mike" in captured.out


def test_cli_input_equals_pure_input_explicit():
    from_cli = clime(Dude, args=["--name", "mike"])
    from_python = Dude(name="mike")
    assert from_cli == from_python


def test_cli_input_equals_pure_input_with_defaults():
    from_cli = clime(Dude, args=[])
    from_python = Dude()
    assert from_cli == from_python
