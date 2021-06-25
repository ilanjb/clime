from enum import Enum
from typing import Any, Type


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
