import attr
import pytest

from clime import clime_field_transformer
from clime import clime
from clime.clime_exceptions import (
    BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults,
)


@attr.s(auto_attribs=True)
class SampleParserBoolAttWithDefaultValue:
    is_cool: bool = False


def test_bool_explict_true():
    args = clime(
        SampleParserBoolAttWithDefaultValue,
        args=[
            "--is-cool",
        ],
    )
    assert args.is_cool is True


def test_bool_implicit_false():
    args = clime(SampleParserBoolAttWithDefaultValue, args=[])
    assert args.is_cool is False


@attr.s(auto_attribs=True)
class SampleParserBoolAttWithoutDefaultValue:
    is_cool: bool


def test_bool_must_have_default():
    with pytest.raises(BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults):
        clime(SampleParserBoolAttWithoutDefaultValue)


@attr.frozen(auto_attribs=True, field_transformer=clime_field_transformer)
class SampleParserBoolAttWithFieldTransformer:
    is_cool: bool = False


def test_bool_gets_bool_converter():
    args = clime(SampleParserBoolAttWithFieldTransformer, args=["--is-cool"])
    assert args.is_cool is True
