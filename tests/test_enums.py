from enum import Enum, auto

import attr

from parseonce import parseonce_field_transformer
from parseonce import parse_once


class Colors(Enum):
    blue = auto()
    green = auto()


@attr.s(auto_attribs=True)
class SampleParserWithEnum:
    color: Colors = attr.ib(converter=Colors.__getattr__)


def test_enums_good_choice_explicit_converter():
    args = parse_once(SampleParserWithEnum, ["green"])
    assert args.color == Colors.green


@attr.frozen(auto_attribs=True, field_transformer=parseonce_field_transformer)
class SampleParserWithEnumWithFieldTransformer:
    color: Colors


def test_enums_get_enum_converter():
    args = parse_once(SampleParserWithEnum, ["green"])
    assert args.color == Colors.green
