from pathlib import Path
from typing import Optional

import attr

from clime.utilities import get_arg_type_for_argparser


def test_get_arg_type_for_argparser_mandatory_str():
    @attr.s(auto_attribs=True)
    class Test:
        name: str

    assert get_arg_type_for_argparser(Test.__attrs_attrs__[0]) == str


def test_get_arg_type_for_argparser_optional_str():
    @attr.s(auto_attribs=True)
    class Test:
        name: Optional[str]

    assert get_arg_type_for_argparser(Test.__attrs_attrs__[0]) == str


def test_get_arg_type_for_argparser_mandatory_path():
    @attr.s(auto_attribs=True)
    class Test:
        filepath: Path

    assert get_arg_type_for_argparser(Test.__attrs_attrs__[0]) == Path
