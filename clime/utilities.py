from enum import Enum
from typing import Any, Type

from attr import Attribute


def field_type_is_of_class(
    field_type: Any,
    klass: Type[object],
):
    """
    :param field_type: taken from attr.Attribute.type
    :param klass: the class to check against

    :return:
    """
    try:
        is_of_class = issubclass(field_type, klass)
    except TypeError:
        is_of_class = False

    return is_of_class


def field_type_is_enum(field_type: Any):
    """
    :param field_type: taken from attr.Attribute.type

    :return:
    """
    return field_type_is_of_class(field_type, Enum)


def field_type_is_class(field_type: Any):
    """
    :param field_type: taken from attr.Attribute.type

    :return:
    """
    return field_type_is_of_class(field_type, object)


def get_arg_type_for_argparser(attribute: Attribute):
    default_arg_type = str

    arg_type = attribute.type
    if field_type_is_class(arg_type):
        return arg_type

    not_none_args = [t for t in arg_type.__args__ if t is not type(None)]
    if not not_none_args:
        return default_arg_type
    if len(not_none_args) > 1:
        return default_arg_type
    arg_type = not_none_args[0]
    return arg_type
