from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import attr

from clime.utilities import field_type_is_enum
from clime.clime_exceptions import (
    BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults,
    BaseClassIsNotAttrs,
)


def add_argument_to_parser(parser: ArgumentParser, field: attr.Attribute) -> None:
    """
    Parses information from that Attribute to add an argument to the parser
    All types will be handled as strings except for booleans!
    conversions should be done via attrs.ib(converter=)
    """
    arg_name = field.name.replace("_", "-")  # this is not working well
    arg_type = field.type
    default = field.default
    help_str = field.metadata.get(
        "help", " "
    )  # default to something so the ArgumentDefaultsHelpFormatter will work.

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


def build_argument_parser(attrs_decorated_class) -> ArgumentParser:
    """
    Creates the parser. then adds the arguments.
    :return:
    """
    parser = ArgumentParser(
        usage=attrs_decorated_class.__doc__,
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    for field in attrs_decorated_class.__attrs_attrs__:
        add_argument_to_parser(parser, field)
    return parser


def clime(attrs_decorated_class, args=None, namespace=None):
    """
    Main api. Turns the class into and parser and returns the and instance of the class.
    :param args:
    :param namespace:
    :return:
    """
    if not hasattr(attrs_decorated_class, "__attrs_attrs__"):
        msg = f"{attrs_decorated_class.__name__} does not look like it has and attrs decorator. This is not going to work :-("
        raise BaseClassIsNotAttrs(msg)
    parser = build_argument_parser(attrs_decorated_class)
    args = parser.parse_args(args=args, namespace=namespace)
    return attrs_decorated_class(**args.__dict__)
