import attr

from attrsargparser.attrsargparser import (
    AttrsArgparser,
    attrs_argparser_field_transformers,
)


@attr.s(auto_attribs=True)
class SampleParserIntAttWithoutDefaultValue(AttrsArgparser):
    age: int = attr.ib(converter=int)


def test_with_int_inputtet_as_str():
    args = SampleParserIntAttWithoutDefaultValue.getargs(
        ["7"]
    )  # input from command line take as str
    assert args.age == 7


@attr.frozen(auto_attribs=True, field_transformer=attrs_argparser_field_transformers)
class SampleParserIntAttWithoutDefaultValueWithFieldTransformer(AttrsArgparser):
    age: int


def test_int_type_gets_int_converter():
    args = SampleParserIntAttWithoutDefaultValueWithFieldTransformer.getargs(["7"])
    assert args.age == 7
