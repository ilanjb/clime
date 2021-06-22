class AttrsArgparserExceptions(Exception):
    pass


class CannotConvertAttrsAttributeToArgparseArgument(AttrsArgparserExceptions):
    pass


class BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults(
    CannotConvertAttrsAttributeToArgparseArgument
):
    pass


class AttrsArgparserFieldTransformerExceptions(AttrsArgparserExceptions):
    pass


class CouldNotAssumeConverter(AttrsArgparserFieldTransformerExceptions):
    pass
