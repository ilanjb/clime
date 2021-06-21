from enum import Enum, auto

import attr

from attrsargparser.attrsargparser import (
    attrs_argparser_field_transformers,
    AttrsArgparser,
)


class Colors(Enum):
    blue = auto()
    green = auto()


@attr.frozen(auto_attribs=True, field_transformer=attrs_argparser_field_transformers)
class SampleParserWithEnum(AttrsArgparser):
    color: Colors = attr.ib()


def test_enum_converter_added():
    assert (
        attr.fields_dict(SampleParserWithEnum)["color"].converter == Colors.__getattr__
    )
