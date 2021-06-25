import attr
import pytest

from clime import clime_field_transformer
from clime import clime


@attr.s(auto_attribs=True)
class SampleParserStrAttNoDefaultValue:
    name: str


def test_first_sample_no_default_means_positional_argument_good():
    args = clime(SampleParserStrAttNoDefaultValue, ["joe"])
    assert isinstance(args, SampleParserStrAttNoDefaultValue)
    assert args.name == "joe"


def test_first_sample_no_default_means_positional_argument_bad():
    with pytest.raises(SystemExit):
        clime(SampleParserStrAttNoDefaultValue, ["--name", "joe"])


@attr.s(auto_attribs=True)
class SampleParserStrAttWithDefaultValue:
    name: str = None


def test_with_default_means_kw_argument_arg_given():
    args = clime(SampleParserStrAttWithDefaultValue, ["--name", "joe"])
    assert args.name == "joe"


def test_with_default_means_kw_argument_no_arg_given():
    args = clime(SampleParserStrAttWithDefaultValue, args=[])
    assert args.name is None


@attr.frozen(auto_attribs=True, field_transformer=clime_field_transformer)
class SampleParserStrAttNoDefaultValueWithFieldTransformer:
    name: str  # string will be get converter string. Which is fine...


def test_str_type_gets_str_converter():
    args = clime(SampleParserStrAttNoDefaultValueWithFieldTransformer, ["joe"])
    assert args.name == "joe"
