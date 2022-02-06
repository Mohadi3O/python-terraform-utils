from terraform_model.types.atomics.number import Number
from terraform_model.types.typify import typify
from terraform_model.types import assertions
from terraform_model.expressions.expression import Expression


class MathExpression(Expression):

    def __init__(self, left, op, right):
        left = typify(left)
        right = typify(right)
        assertions.is_number(left)
        assertions.is_number(right)
        super().__init__(left, op, right)

    def __str__(self):
        return f'({self.left} {self.op} {self.right})'

    @property
    def left(self):
        return self._args[0]

    @property
    def op(self):
        return self._args[1]

    @property
    def right(self):
        return self._args[2]


def math(left, op, right) -> Number:
    return MathExpression(left, op, right).to_number()
