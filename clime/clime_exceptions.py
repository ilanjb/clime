class CliMeExceptions(Exception):
    pass


class BaseClassIsNotAttrs(CliMeExceptions):
    pass


class CannotConvertAttrsAttributeToArgparseArgument(CliMeExceptions):
    pass


class BooleanArgumentsCannotBePositionalSoTheyMustHaveDefaults(
    CannotConvertAttrsAttributeToArgparseArgument
):
    pass


class ClassesCanOnlyHaveOneInitArgumentBesidesSelfToBeConverted(
    CannotConvertAttrsAttributeToArgparseArgument
):
    pass
