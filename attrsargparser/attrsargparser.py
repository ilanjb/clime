from argparse import ArgumentParser
from enum import Enum
from typing import Any

import attr

from attrsargparser.attrsarparser_exceptions import (
    BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults,
)


def field_type_is_enum(field_type: Any):
    """
    :param field_type: taken from attr.Attribute.type

    :return:
    """
    try:
        is_enum = issubclass(field_type, Enum)
    except TypeError:
        is_enum = False

    return is_enum


def attrs_argparser_field_transformers(cls, fields):
    """
    adapted from https://www.attrs.org/en/stable/extending.html#automatic-field-transformation-and-modification
    sets default convererters

    :param cls:
    :param fields:
    :return:
    """
    results = []
    for field in fields:
        if field.converter is not None:
            results.append(field)
            continue

        if field_type_is_enum(field.type):
            converter = field.type.__getattr__

        else:
            converter = None
        results.append(field.evolve(converter=converter))
    return results


class AttrsArgparser:
    @staticmethod
    def _add_argument_to_parser(parser: ArgumentParser, field: attr.Attribute) -> None:
        """
        Parses information from that Attribute to add an argument to the parser
        All types will be handled as strings except for booleans!
        conversions should be done via attrs.ib(converter=)
        """
        arg_name = field.name.replace("_", "-")  # this is not working well
        arg_type = field.type
        default = field.default
        help_str = field.metadata.get("help", "")

        kwargs = {
            "help": help_str,
        }

        if default != attr.NOTHING:  # handle as optional / non-positional
            arg_name = f"--{arg_name}"

        treat_as_enum = field_type_is_enum(arg_type)

        if treat_as_enum:
            choices = arg_type._member_names_
            kwargs["choices"] = choices
            if default:
                kwargs["default"] = default.name

        elif arg_type == bool:
            if default is False:
                action = "store_true"
            elif default is True:
                action = "store_false"
            else:
                msg = f"{field.name} has no default value"
                raise BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults(msg)
            kwargs["action"] = action

        else:
            kwargs["default"] = default

        parser.add_argument(arg_name, **kwargs)

    @classmethod
    def _build_argument_parser(cls) -> ArgumentParser:
        """
        Creates the parser. then adds the arguments.
        :return:
        """
        parser = ArgumentParser(usage=cls.__doc__)
        for field in cls.__attrs_attrs__:
            cls._add_argument_to_parser(parser, field)
        return parser

    @classmethod
    def getargs(cls, args=None, namespace=None):
        """
        Main api. Turns the class into and parser and returns the and instance of the class.
        :param args:
        :param namespace:
        :return:
        """
        parser = cls._build_argument_parser()
        args = parser.parse_args(args=args, namespace=namespace)
        return cls(**args.__dict__)
