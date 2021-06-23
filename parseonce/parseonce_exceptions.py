class ParseonceExceptions(Exception):
    pass


class BaseClassIsNotAttrs(ParseonceExceptions):
    pass


class CannotConvertAttrsAttributeToArgparseArgument(ParseonceExceptions):
    pass


class BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults(
    CannotConvertAttrsAttributeToArgparseArgument
):
    pass


class FieldTransformerExceptions(ParseonceExceptions):
    pass


class CouldNotAssumeConverter(FieldTransformerExceptions):
    pass
