import attr

from parseonce import parseonce_field_transformer
from parseonce import parse_once


@attr.s(auto_attribs=True)
class SampleParserIntAttWithoutDefaultValue:
    age: int = attr.ib(converter=int)


def test_with_int_inputtet_as_str():
    args = parse_once(
        SampleParserIntAttWithoutDefaultValue, ["7"]
    )  # input from command line take as str
    assert args.age == 7


@attr.frozen(auto_attribs=True, field_transformer=parseonce_field_transformer)
class SampleParserIntAttWithoutDefaultValueWithFieldTransformer:
    age: int


def test_int_type_gets_int_converter():
    args = parse_once(SampleParserIntAttWithoutDefaultValueWithFieldTransformer, ["7"])
    assert args.age == 7
