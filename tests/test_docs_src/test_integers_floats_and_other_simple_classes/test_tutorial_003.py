import sys

from docs_src.integers_floats_and_other_simple_classes.tutorial_003 import main, Dude


def test_correct_input(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("yes i am")
    main()
