import attr
import pytest

from parseonce.parseonce import (
    OnceParser,
    parseonce_field_transformer,
)
from parseonce.parseonce_exceptions import (
    BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults,
)


@attr.s(auto_attribs=True)
class SampleParserBoolAttWithDefaultValue(OnceParser):
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
class SampleParserBoolAttWithoutDefaultValue(OnceParser):
    is_cool: bool


def test_bool_must_have_default():
    with pytest.raises(BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults):
        SampleParserBoolAttWithoutDefaultValue.getargs()


@attr.frozen(auto_attribs=True, field_transformer=parseonce_field_transformer)
class SampleParserBoolAttWithFieldTransformer(OnceParser):
    is_cool: bool = False


def test_bool_gets_bool_converter():
    args = SampleParserBoolAttWithFieldTransformer.getargs(args=["--is-cool"])
    assert args.is_cool is True
