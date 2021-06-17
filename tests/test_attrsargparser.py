import attr
import pytest

from attrsargparser.attrsargparser import AttrsArgparser


@attr.s(auto_attribs=True)
class SampleParserStrAttNoDefaultValue(AttrsArgparser):
    name: str


@attr.s(auto_attribs=True)
class SampleParserStrAttWithDefaultValue(AttrsArgparser):
    name: str


def test_first_sample_no_default_means_positional_argument_good():
    args: SampleParserStrAttNoDefaultValue.getargs(["joe"])
    assert isinstance(args, SampleParserStrAttNoDefaultValue)
    assert args.name == "joe"


def test_first_sample_no_default_means_positional_argument_bad():
    with pytest.raises(SystemExit):
        SampleParserStrAttNoDefaultValue.getargs(["--name", "joe"])


def test_with_default_means_kw_argument():
    args: SampleParserStrAttWithDefaultValue.getargs(["--name", "joe"])
    assert args.name == "joe"
