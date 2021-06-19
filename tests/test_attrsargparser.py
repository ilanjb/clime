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
