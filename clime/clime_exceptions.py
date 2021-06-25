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


class FieldTransformerExceptions(CliMeExceptions):
    pass


class CouldNotAssumeConverter(FieldTransformerExceptions):
    pass
