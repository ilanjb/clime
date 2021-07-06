import sys

import pytest

from clime import clime
from docs_src.enums.tutorial_001 import main, Dude, Colors


def test_help(set_cli_sys_argv, capsys):
    sys.argv.append("--help")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "{Colors.red,Colors.blue}" in captured.out  # I wish it were just {red,blue}
    """
    usage: tutorial_001.py [-h] {Colors.red,Colors.blue}
    
    positional arguments:
      {Colors.red,Colors.blue}
                            type: <Colors>
    
    optional arguments:
      -h, --help            show this help message and exit
    """


def test_good_choice(set_cli_sys_argv, capsys):
    sys.argv.append("blue")
    main()
    captured = capsys.readouterr()
    assert "my favorite color is blue" in captured.out


def test_bad_choice(set_cli_sys_argv, capsys):
    sys.argv.append("circles")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "argument favorite_color: invalid Colors value: 'circles'" in captured.err


def test_cli_input_equals_pure_input():
    from_cli = clime(Dude, args=["blue"])
    from_python = Dude(Colors.blue)
    assert from_cli == from_python
