import sys

from docs_src.strings.tutorial_002 import main

def test_args_inputted_properly(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("joe")
    main()
    captured = capsys.readouterr()
    assert captured.out == "hi! my name is Joe\n"