import attr
import pytest

from attrsargparser.attrsargparser import (
    AttrsArgparser,
    attrs_argparser_field_transformers,
)


@attr.s(auto_attribs=True)
class SampleParserIntAttWithoutDefaultValue(AttrsArgparser):
    age: float = attr.ib(converter=float)


def test_with_float_with_decimal():
    args = SampleParserIntAttWithoutDefaultValue.getargs(["7.35"])
    assert args.age == 7.35


def test_with_float_with_no_decimal():
    args = SampleParserIntAttWithoutDefaultValue.getargs(["7"])
    assert args.age == 7.0


def test_catch_not_a_float():
    with pytest.raises(ValueError, match="could not convert string to float"):
        SampleParserIntAttWithoutDefaultValue.getargs(["seven"])


@attr.frozen(auto_attribs=True, field_transformer=attrs_argparser_field_transformers)
class SampleParserIntAtteWithFieldTransformer(AttrsArgparser):
    age: float


def test_float_gets_float_converter():
    args = SampleParserIntAtteWithFieldTransformer.getargs(["7.35"])
    assert args.age == 7.35
