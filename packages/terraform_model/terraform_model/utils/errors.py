class TerraformModelException(Exception):
    pass


class TerraformConversionError(TerraformModelException):
    pass


class TerraformTypeError(TerraformModelException):
    pass
