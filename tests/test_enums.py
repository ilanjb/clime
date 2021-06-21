from enum import Enum, auto

import attr

from attrsargparser.attrsargparser import (
    AttrsArgparser,
    attrs_argparser_field_transformers,
)


class Colors(Enum):
    blue = auto()
    green = auto()


@attr.s(auto_attribs=True)
class SampleParserWithEnum(AttrsArgparser):
    color: Colors = attr.ib(converter=Colors.__getattr__)


def test_enums_good_choice_explicit_converter():
    args = SampleParserWithEnum.getargs(["green"])
    assert args.color == Colors.green


@attr.frozen(auto_attribs=True, field_transformer=attrs_argparser_field_transformers)
class SampleParserWithEnumWithattrs_argparser_field_transformers(AttrsArgparser):
    color: Colors


def test_enums_good_choice_implicit_converter_from_attrs_argparser_field_transformers():
    args = SampleParserWithEnum.getargs(["green"])
    assert args.color == Colors.green
