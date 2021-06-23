import attr
import pytest

from parseonce.onceparser import OnceParser


@attr.s(auto_attribs=True)
class SampleParserWithHelp(OnceParser):
    name: str = attr.ib(metadata={"help": "help me!"})


def test_help_works(capsys):
    with pytest.raises(SystemExit):
        SampleParserWithHelp.getargs(["--help"])
    captured = capsys.readouterr()
    assert "help me!" in captured.out
