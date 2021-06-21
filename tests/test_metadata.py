import attr
import pytest

from attrsargparser.attrsargparser import AttrsArgparser


@attr.s(auto_attribs=True)
class SampleParserWithHelp(AttrsArgparser):
    name: str = attr.ib(metadata={"help": "help me!"})


def test_help_works(capsys):
    with pytest.raises(SystemExit):
        SampleParserWithHelp.getargs(["--help"])
    captured = capsys.readouterr()
    assert "help me!" in captured.out