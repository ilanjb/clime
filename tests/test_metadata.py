import attr
import pytest

from clime import clime


@attr.s(auto_attribs=True)
class SampleParserWithHelp:
    name: str = attr.ib(metadata={"help": "help me!"})


def test_help_works(capsys):
    with pytest.raises(SystemExit):
        clime(SampleParserWithHelp, ["--help"])
    captured = capsys.readouterr()
    assert "help me!" in captured.out
