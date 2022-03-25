from terraform_model.types.primitives.tfbool import TfBool
from terraform_model.types.conversions.typify import typify
from terraform_model.internal import tfassert
from terraform_model.expressions.expressions.math import MathExpression


class Logical(MathExpression):

    def __init__(self, left, op, right):
        left = typify(left)
        right = typify(right)
        tfassert.is_bool(left)
        tfassert.is_bool(right)
        super().__init__(left, op, right)

    def __str__(self):
        return f'({self.left} {self.op} {self.right})'


def logical(left, op, right) -> TfBool:
    return Logical(left, op, right).to_bool()
