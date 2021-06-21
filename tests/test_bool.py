import attr
import pytest

from attrsargparser.attrsargparser import AttrsArgparser
from attrsargparser.attrsarparser_exceptions import BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults


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