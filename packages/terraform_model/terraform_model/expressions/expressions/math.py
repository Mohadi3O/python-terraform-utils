from terraform_model.types.primitives.tfnumber import TfNumber
from terraform_model.types.conversions.typify import typify
from terraform_model.expressions.expression import Expression


class MathExpression(Expression):

    def __init__(self, left, op, right):
        left = typify(left)
        right = typify(right)
        super().__init__(left, op, right)

    def __str__(self):
        return f'({self.left} {self.op} {self.right})'

    @property
    def left(self):
        return self._args[0]

    @property
    def op(self):
        return self._args[1].data

    @property
    def right(self):
        return self._args[2]


def math(left, op, right) -> TfNumber:
    return MathExpression(left, op, right).to_number()
