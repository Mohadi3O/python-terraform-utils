from terraform_model.types.atomics.bool import Bool
from terraform_model.types.typify import typify
from terraform_model.types import assertions
from terraform_model.expressions.expressions.math import MathExpression


class Compare(MathExpression):

    def __init__(self, left, op, right):
        left = typify(left)
        right = typify(right)
        assertions.same_type(left, right)
        super().__init__(left, op, right)

    def __str__(self):
        return f'({self.left} {self.op} {self.right})'


def compare(left, op, right) -> Bool:
    return Compare(left, op, right).to_bool()
