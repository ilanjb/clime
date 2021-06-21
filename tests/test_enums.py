from enum import Enum, auto

import attr

from attrsargparser.attrsargparser import AttrsArgparser


class Colors(Enum):
    blue = auto()
    green = auto()


@attr.s(auto_attribs=True, frozen=False, eq=False)
class SampleParserWithEnum(AttrsArgparser):
    color: Colors = attr.ib(
        converter=Colors.__getattr__
    )  # this should be auto generated


def test_enums_good_choice():
    args = SampleParserWithEnum.getargs(["green"])
    assert args.color == Colors.green