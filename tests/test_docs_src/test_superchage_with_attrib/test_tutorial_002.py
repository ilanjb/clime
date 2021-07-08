import sys

import pytest

from docs_src.supercharge_with_attrib.tutorial_002 import main


def test_input_valid(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("10")
    main()
    captured = capsys.readouterr()
    assert captured.out == "My favorite number less than 100 is 10\n"


def test_input_not_valid(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("101")
    with pytest.raises(
        ValueError, match="favorite_number_less_than_100 has to be smaller than 100!"
    ):
        main()
