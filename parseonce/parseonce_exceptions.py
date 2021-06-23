class ParseonceExceptions(Exception):
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
