from typing import Iterable
import logging

import attr

from parseonce.configs import KNOWN_CLASS_TYPES_THAT_WILL_WORK_WELL
from parseonce.utilities import field_type_is_enum, field_type_is_class
from parseonce.parseonce_exceptions import CouldNotAssumeConverter


LOGGER = logging.Logger(__name__)


def parseonce_field_transformer(cls, fields: Iterable[attr.Attribute]):
    """
    adapted from https://www.attrs.org/en/stable/extending.html#automatic-field-transformation-and-modification
    sets default converters

    :param cls:
    :param fields:
    :return:
    """
    results = []
    for field in fields:
        if field.converter is not None:
            msg = f"field {field.name} with explicit converter {field.converter} left as is"
            LOGGER.debug(msg)
            results.append(field)
            continue

        if field_type_is_enum(field.type):
            msg = f"enum like field {field.name} with being given {field.type.__getattr__} converter"
            LOGGER.debug(msg)
            converter = field.type.__getattr__

        elif field.type in KNOWN_CLASS_TYPES_THAT_WILL_WORK_WELL:
            msg = f"{field.name} with type {field.type} being given {field.type} converter"
            LOGGER.debug(msg)
            converter = field.type

        elif field_type_is_class(field.type):
            msg = f"{field.name} with type {field.type} being given {field.type} converter. Not so sure this is going to work... Use explicit converter if you need."
            LOGGER.debug(msg)
            converter = field.type

        else:
            msg = f" Could not assume converted for {field.name} with type {field.type}. Use explicit converter."
            raise CouldNotAssumeConverter(msg)

        results.append(field.evolve(converter=converter))
    return results
