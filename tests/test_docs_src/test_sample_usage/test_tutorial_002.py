import sys

import pytest

from docs_src.sample_usage.tutorial_002 import main


def test_help(set_cli_sys_argv, capsys):
    sys.argv.append("--help")
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()

    assert captured.out == (
        """usage: 
    Everything about the Dude!
    

positional arguments:
  name                  type: <str>
  {Colors.red,Colors.blue}
                        type: <Colors>

optional arguments:
  -h, --help            show this help message and exit
  --age-in-years AGE_IN_YEARS
                        type: <int> (default: None)
"""
    )


def test_good(set_cli_sys_argv, capsys):
    sys.argv.extend(["joe", "red", "--age-in-years", "15"])
    main()
    captured = capsys.readouterr()

    assert captured.out == (
        """hi! my name is joe
my favorite color is red
I am 15 years old.
"""
    )
