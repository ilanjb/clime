from random import random

import attr
import pytest

from clime import clime
from clime.clime_exceptions import BaseClassIsNotAttrs


@attr.s(auto_attribs=True)
class SampleParserStrAttNoDefaultValue:
    name: str


def test_default_means_positional_argument_bad(capsys):
    with pytest.raises(SystemExit):
        clime(SampleParserStrAttNoDefaultValue, ["--name", "joe"])
    captured = capsys.readouterr()
    assert "unrecognized arguments: --name" in captured.err


@attr.s(auto_attribs=True)
class SampleParserWithNonInitField:
    name: str
    secret: int = attr.ib(init=False, factory=random)


def test_non_init_fields_not_in_parser(capsys):
    with pytest.raises(SystemExit):
        clime(SampleParserStrAttNoDefaultValue, ["joe", "123"])
    captured = capsys.readouterr()
    assert "unrecognized arguments: 123" in captured.err


@attr.s(auto_attribs=True)
class SampleParserWithDocstings:
    """Hi. This is great"""

    name: str


def test_docsrings_are_used_for_usage(capsys):
    with pytest.raises(SystemExit):
        clime(SampleParserWithDocstings, ["--help"])
    captured = capsys.readouterr()
    assert "usage: Hi. This is great" in captured.out


class ForgotAttrsDecorator:
    """Hi. This is great"""

    name: str


def test_good_catch_on_non_attr_class():
    with pytest.raises(BaseClassIsNotAttrs, match="not going to work"):
        clime(ForgotAttrsDecorator)
