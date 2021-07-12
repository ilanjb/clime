from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from inspect import signature

import attr

from clime.configs import KNOWN_CLASS_TYPES_THAT_WILL_WORK_WELL
from clime.utilities import field_type_is_enum, get_arg_type_for_argparser
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

    arg_type = get_arg_type_for_argparser(field)

    default = field.default

    custom_help = field.metadata.get("help", "")

    type_help = f"type: <{arg_type.__name__}>"

    help_str = f"{custom_help} {type_help}"

    kwargs = {
        "help": help_str,
    }

    # positonal / optional handling
    if default != attr.NOTHING:  # handle as optional / non-positional
        arg_name = field.name.replace("_", "-")  # will be changed back
        arg_name = f"--{arg_name}"

    else:
        arg_name = field.name
        default = None  # safe to pass to add_argument()
        if custom_help:
            kwargs["help"] = custom_help  # dont force help.

    # type handling

    treat_as_enum = field_type_is_enum(arg_type)
    if field.converter:  # user can convert howerver they want. Keep type out of it.
        pass

    elif treat_as_enum:
        # as suggested by rhettinger https://bugs.python.org/issue25061#msg350853
        # note that the choices are presented as {ClassName.name,} which is unfortunale
        choices = arg_type
        kwargs["choices"] = choices
        if default:
            kwargs["default"] = default.name  # will be converted back
        kwargs["type"] = arg_type

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
        if arg_type not in KNOWN_CLASS_TYPES_THAT_WILL_WORK_WELL:
            init_signature = signature(arg_type.__init__, follow_wrapped=True)
            # check
        kwargs["type"] = arg_type
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
