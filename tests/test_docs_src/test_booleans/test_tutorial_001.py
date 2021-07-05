import sys

import pytest

from clime import clime
from docs_src.booleans.tutorial_001 import main, Dude


def test_help(set_cli_sys_argv, capsys):
    sys.argv.append("-h")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "optional arguments" in captured.out
    assert "--likes-ice-cream  (default: False)"

    """
    should look like this:
    usage: tutorial_001.py [-h] [--likes-ice-cream]
    
    optional arguments:
      -h, --help         show this help message and exit
      --likes-ice-cream  (default: False)

    """


def test_defaults_to_false(set_cli_sys_argv, capsys):
    main()
    captured = capsys.readouterr()
    assert "hi! i do not like ice cream" in captured.out


def test_flag_sets_true(set_cli_sys_argv, capsys):
    sys.argv.append("--likes-ice-cream")
    main()
    captured = capsys.readouterr()
    assert "hi! i like ice cream" in captured.out


def test_cli_input_equals_pure_input_no_args():
    from_cli = clime(Dude, args=[])
    from_python = Dude()
    assert from_cli == from_python


def test_cli_input_equals_pure_input_no_args():
    from_cli = clime(Dude, args=["--likes-ice-cream"])
    from_python = Dude(likes_ice_cream=True)
    assert from_cli == from_python
