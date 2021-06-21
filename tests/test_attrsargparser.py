from enum import Enum, auto

import attr
import pytest

from attrsargparser.attrsargparser import AttrsArgparser
from attrsargparser.attrsarparser_exceptions import (
    BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults,
)


@attr.s(auto_attribs=True)
class SampleParserStrAttNoDefaultValue(AttrsArgparser):
    name: str


def test_first_sample_no_default_means_positional_argument_good():
    args = SampleParserStrAttNoDefaultValue.getargs(["joe"])
    assert isinstance(args, SampleParserStrAttNoDefaultValue)
    assert args.name == "joe"


def test_first_sample_no_default_means_positional_argument_bad():
    with pytest.raises(SystemExit):
        SampleParserStrAttNoDefaultValue.getargs(["--name", "joe"])


@attr.s(auto_attribs=True)
class SampleParserStrAttWithDefaultValue(AttrsArgparser):
    name: str = None


def test_with_default_means_kw_argument_arg_given():
    args = SampleParserStrAttWithDefaultValue.getargs(["--name", "joe"])
    assert args.name == "joe"


def test_with_default_means_kw_argument_no_arg_given():
    args = SampleParserStrAttWithDefaultValue.getargs([])
    assert args.name is None


@attr.s(auto_attribs=True)
class SampleParserIntAttWithoutDefaultValue(AttrsArgparser):
    age: int


def test_with_int_inputtet_as_str():
    args = SampleParserIntAttWithoutDefaultValue.getargs(
        ["7"]
    )  # input from command line take as str
    assert args.age == 7


@attr.s(auto_attribs=True)
class SampleParserBoolAttWithDefaultValue(AttrsArgparser):
    is_cool: bool = False


def test_bool_explict_true():
    args = SampleParserBoolAttWithDefaultValue.getargs(
        args=[
            "--is-cool",
        ]
    )
    assert args.is_cool is True


def test_bool_implict_false():
    args = SampleParserBoolAttWithDefaultValue.getargs(args=[])
    assert args.is_cool is False


@attr.s(auto_attribs=True)
class SampleParserBoolAttWithoutDefaultValue(AttrsArgparser):
    is_cool: bool


def test_bool_must_have_default():
    with pytest.raises(BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults):
        SampleParserBoolAttWithoutDefaultValue.getargs()


@attr.s(auto_attribs=True)
class SampleParserWithHelp(AttrsArgparser):
    name: str = attr.ib(metadata={"help": "help me!"})


def test_help_works(capsys):
    with pytest.raises(SystemExit):
        SampleParserWithHelp.getargs(["--help"])
    captured = capsys.readouterr()
    assert "help me!" in captured.out


class Colors(Enum):
    blue = auto()
    green = auto()


@attr.s(auto_attribs=True, frozen=False, eq=False)
class SampleParserWithEnum(AttrsArgparser):
    color: Colors = attr.ib(
        converter=Colors.__getattr__
    )  # this should be auto generated


def test_enums_good_choice():
    args = SampleParserWithEnum.getargs(["green"])
    assert args.color == Colors.green
