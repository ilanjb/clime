import attr
import pytest

from parseonce import parse_once


@attr.s(auto_attribs=True)
class SampleParserWithHelp:
    name: str = attr.ib(metadata={"help": "help me!"})


def test_help_works(capsys):
    with pytest.raises(SystemExit):
        parse_once(SampleParserWithHelp, ["--help"])
    captured = capsys.readouterr()
    assert "help me!" in captured.out
