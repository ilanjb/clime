import sys

import pytest

from docs_src.supercharge_with_attrib.tutorial_003 import main


def test_input_valid(set_cli_sys_argv, capsys):
    """
    date will be converted to datetime.date
    """
    sys.argv.append("2000-11-22")  # seams okay
    main()
    captured = capsys.readouterr()
    assert captured.out == "My birthday is 2000-11-22\n"


def test_input_not_valid(set_cli_sys_argv, capsys):
    """
    what if the date is invalid?
    """
    sys.argv.append("2000-13-22")  # not a valid date
    with pytest.raises(
        ValueError, match="time data '2000-13-22' does not match format '%Y-%m-%d'"
    ):
        main()
