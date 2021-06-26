import sys

import pytest

from docs_src.strings.tutorial_001 import main


def test_help(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("-h")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert (
        captured.out
        == "usage: _jb_pytest_runner.py [-h] name\n\npositional arguments:\n  name\n\noptional arguments:\n  -h, --help  show this help message and exit\n"
    )


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
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "error: the following arguments are required: name" in captured.err


def test_args_inputted_properly(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("joe")
    main()
    captured = capsys.readouterr()
    assert captured.out == "hi! my name is joe\n"
