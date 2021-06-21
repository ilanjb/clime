class AttrsArgparserExceptions(Exception):
    pass


class CannotConvertAttrsAttributeToArgparseArgument(AttrsArgparserExceptions):
    pass


class BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults(
    CannotConvertAttrsAttributeToArgparseArgument
):
    pass
