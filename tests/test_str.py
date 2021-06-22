import attr
import pytest

from attrsargparser.attrsargparser import (
    AttrsArgparser,
    attrs_argparser_field_transformers,
)


@attr.s(auto_attribs=True)
class SampleParserStrAttNoDefaultValue(AttrsArgparser):
    name: str


def test_first_sample_no_default_means_positional_argument_good():
    args = SampleParserStrAttNoDefaultValue.getargs(["joe"])
    assert isinstance(args, SampleParserStrAttNoDefaultValue)
    assert args.name == "joe"


def test_first_sample_no_default_means_positional_argument_bad():
    with pytest.raises(SystemExit):
        SampleParserStrAttNoDefaultValue.getargs(["--name", "joe"])


@attr.s(auto_attribs=True)
class SampleParserStrAttWithDefaultValue(AttrsArgparser):
    name: str = None


def test_with_default_means_kw_argument_arg_given():
    args = SampleParserStrAttWithDefaultValue.getargs(["--name", "joe"])
    assert args.name == "joe"


def test_with_default_means_kw_argument_no_arg_given():
    args = SampleParserStrAttWithDefaultValue.getargs([])
    assert args.name is None


@attr.frozen(auto_attribs=True, field_transformer=attrs_argparser_field_transformers)
class SampleParserStrAttNoDefaultValueWithFieldTransformer(AttrsArgparser):
    name: str  # strint will be get converter string. Which is fine...


def test_str_type_gets_str_converter():
    args = SampleParserStrAttNoDefaultValueWithFieldTransformer.getargs(["joe"])
    assert args.name == "joe"
