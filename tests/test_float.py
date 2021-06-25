import attr
import pytest

from clime import clime_field_transformer
from clime import clime


@attr.s(auto_attribs=True)
class SampleParserIntAttWithoutDefaultValue:
    age: float = attr.ib(converter=float)


def test_with_float_with_decimal():
    args = clime(SampleParserIntAttWithoutDefaultValue, ["7.35"])
    assert args.age == 7.35


def test_with_float_with_no_decimal():
    args = clime(SampleParserIntAttWithoutDefaultValue, ["7"])
    assert args.age == 7.0


def test_catch_not_a_float():
    with pytest.raises(ValueError, match="could not convert string to float"):
        clime(SampleParserIntAttWithoutDefaultValue, ["seven"])


@attr.frozen(auto_attribs=True, field_transformer=clime_field_transformer)
class SampleParserIntAtteWithFieldTransformer:
    age: float


def test_float_gets_float_converter():
    args = clime(SampleParserIntAtteWithFieldTransformer, ["7.35"])
    assert args.age == 7.35
