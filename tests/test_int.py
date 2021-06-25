import attr

from clime import clime_field_transformer
from clime import clime


@attr.s(auto_attribs=True)
class SampleParserIntAttWithoutDefaultValue:
    age: int = attr.ib(converter=int)


def test_with_int_inputtet_as_str():
    args = clime(
        SampleParserIntAttWithoutDefaultValue, ["7"]
    )  # input from command line take as str
    assert args.age == 7


@attr.frozen(auto_attribs=True, field_transformer=clime_field_transformer)
class SampleParserIntAttWithoutDefaultValueWithFieldTransformer:
    age: int


def test_int_type_gets_int_converter():
    args = clime(SampleParserIntAttWithoutDefaultValueWithFieldTransformer, ["7"])
    assert args.age == 7
