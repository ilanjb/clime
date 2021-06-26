import pytest

from docs_src.strings.tutorial_001 import main


def test_no_args(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "error: the following arguments are required: name" in captured.err
