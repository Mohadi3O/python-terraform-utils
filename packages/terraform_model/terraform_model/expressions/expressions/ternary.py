# internal
from terraform_model.types.internal.tftype import TfType
from terraform_model.types.conversions.typify import to, typify
from terraform_model.internal import tfassert
from terraform_model.expressions.expression import Expression


class Ternary(Expression):

    def __init__(self, condition, true_val, false_val):
        true_val = typify(true_val)
        false_val = typify(false_val)
        tfassert.same_type(true_val, false_val)
        super().__init__(condition, true_val, false_val)

    def __str__(self):
        return f'({self.condition} ? {self.true_val} : {self.false_val})'

    @property
    def condition(self):
        return self.str(self._args[0])

    @property
    def true_val(self):
        return self.str(self._args[1])

    @property
    def false_val(self):
        return self.str(self._args[2])


def ternary(condition, true_val, false_val) -> TfType:
    t = Ternary(condition, true_val, false_val)
    return to(t, true_val)
