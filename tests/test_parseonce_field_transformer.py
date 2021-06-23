from enum import Enum, auto

import attr

from parseonce.parseonce import (
    parseonce_field_transformer,
    OnceParser,
)


class Colors(Enum):
    blue = auto()
    green = auto()


@attr.frozen(auto_attribs=True, field_transformer=parseonce_field_transformer)
class SampleParserWithEnum(OnceParser):
    color: Colors = attr.ib()


def test_enum_converter_added():
    assert (
        attr.fields_dict(SampleParserWithEnum)["color"].converter == Colors.__getattr__
    )
