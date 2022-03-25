# internal
from terraform_model.utils.expression import expression


class ExpressionMixin:

    def __format__(self, format_spec):
        return self.expression() if format_spec == '$' else str(self)

    def expression(self) -> str:
        return expression(str(self))
