# internal
from terraform_model.utils.expression import expression


class ExpressionMixin:

    def expression(self) -> str:
        return expression(str(self))
