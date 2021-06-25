from enum import Enum, auto

import attr

from clime import clime_field_transformer


class Colors(Enum):
    blue = auto()
    green = auto()


@attr.frozen(auto_attribs=True, field_transformer=clime_field_transformer)
class SampleParserWithEnum:
    color: Colors = attr.ib()


def test_enum_converter_added():
    assert (
        attr.fields_dict(SampleParserWithEnum)["color"].converter == Colors.__getattr__
    )
