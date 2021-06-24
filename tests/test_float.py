import attr
import pytest

from parseonce import parseonce_field_transformer
from parseonce import parse_once


@attr.s(auto_attribs=True)
class SampleParserIntAttWithoutDefaultValue:
    age: float = attr.ib(converter=float)


def test_with_float_with_decimal():
    args = parse_once(SampleParserIntAttWithoutDefaultValue, ["7.35"])
    assert args.age == 7.35


def test_with_float_with_no_decimal():
    args = parse_once(SampleParserIntAttWithoutDefaultValue, ["7"])
    assert args.age == 7.0


def test_catch_not_a_float():
    with pytest.raises(ValueError, match="could not convert string to float"):
        parse_once(SampleParserIntAttWithoutDefaultValue, ["seven"])


@attr.frozen(auto_attribs=True, field_transformer=parseonce_field_transformer)
class SampleParserIntAtteWithFieldTransformer:
    age: float


def test_float_gets_float_converter():
    args = parse_once(SampleParserIntAtteWithFieldTransformer, ["7.35"])
    assert args.age == 7.35
