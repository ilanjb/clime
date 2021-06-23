from random import random

import attr
import pytest

from parseonce import OnceParser
from parseonce.parseonce_exceptions import BaseClassIsNotAttrs


@attr.s(auto_attribs=True)
class SampleParserStrAttNoDefaultValue(OnceParser):
    name: str


def test_default_means_positional_argument_bad(capsys):
    with pytest.raises(SystemExit):
        SampleParserStrAttNoDefaultValue.getargs(["--name", "joe"])
    captured = capsys.readouterr()
    assert "unrecognized arguments: --name" in captured.err


@attr.s(auto_attribs=True)
class SampleParserWithNonInitField(OnceParser):
    name: str
    secret: int = attr.ib(init=False, factory=random)


def test_non_init_fields_not_in_parser(capsys):
    with pytest.raises(SystemExit):
        SampleParserStrAttNoDefaultValue.getargs(["joe", "123"])
    captured = capsys.readouterr()
    assert "unrecognized arguments: 123" in captured.err


@attr.s(auto_attribs=True)
class SampleParserWithDocstings(OnceParser):
    """Hi. This is great"""

    name: str


def test_docsrings_are_used_for_usage(capsys):
    with pytest.raises(SystemExit):
        SampleParserWithDocstings.getargs(["--help"])
    captured = capsys.readouterr()
    assert "usage: Hi. This is great" in captured.out


class ForgotAttrsDecorator(OnceParser):
    """Hi. This is great"""

    name: str


def test_good_catch_on_non_attr_class():
    with pytest.raises(BaseClassIsNotAttrs, match="not going to work"):
        ForgotAttrsDecorator.getargs()
