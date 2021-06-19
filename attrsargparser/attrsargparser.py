from argparse import ArgumentParser
from typing import Any

import attr

from attrsargparser.attrsarparser_exceptions import (
    BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults,
)


@attr.s(auto_attribs=True)
class AttrsArgparser:
    @staticmethod
    def _add_argument_to_parser(
        parser: ArgumentParser, attibute_arument: attr.Attribute
    ) -> None:
        """
        Parses information from that Attribute to add an argument to the parser
        """
        arg_name = attibute_arument.name.replace("_", "-")
        arg_type = attibute_arument.type
        default = attibute_arument.default

        kwargs = {
            "type": arg_type,
            "default": default,
        }

        if default != attr.NOTHING:  # handle as optional / non-positional
            arg_name = f"--{arg_name}"

        if arg_type == bool:
            if default is False:
                action = "store_true"
            elif default is True:
                action = "store_false"
            else:
                msg = f"{attibute_arument.name} has no default value"
                raise BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults(msg)
            kwargs["action"] = action
            kwargs.pop("type")
            kwargs.pop("default")

        parser.add_argument(arg_name, **kwargs)

    @classmethod
    def _build_argument_parser(cls) -> ArgumentParser:
        """
        Creates the parser. then adds the arguments.
        :return:
        """
        parser = ArgumentParser()
        for attibute_arument in cls.__attrs_attrs__:
            cls._add_argument_to_parser(parser, attibute_arument)
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
