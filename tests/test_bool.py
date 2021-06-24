import attr
import pytest

from parseonce import parseonce_field_transformer
from parseonce import parse_once
from parseonce.parseonce_exceptions import (
    BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults,
)


@attr.s(auto_attribs=True)
class SampleParserBoolAttWithDefaultValue:
    is_cool: bool = False


def test_bool_explict_true():
    args = parse_once(
        SampleParserBoolAttWithDefaultValue,
        args=[
            "--is-cool",
        ],
    )
    assert args.is_cool is True


def test_bool_implict_false():
    args = parse_once(SampleParserBoolAttWithDefaultValue, args=[])
    assert args.is_cool is False


@attr.s(auto_attribs=True)
class SampleParserBoolAttWithoutDefaultValue:
    is_cool: bool


def test_bool_must_have_default():
    with pytest.raises(BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults):
        parse_once(SampleParserBoolAttWithoutDefaultValue)


@attr.frozen(auto_attribs=True, field_transformer=parseonce_field_transformer)
class SampleParserBoolAttWithFieldTransformer:
    is_cool: bool = False


def test_bool_gets_bool_converter():
    args = parse_once(SampleParserBoolAttWithFieldTransformer, args=["--is-cool"])
    assert args.is_cool is True
