# std
from typing import Union

# internal
from terraform_model import conf
from terraform_model.types.primitives.tfbool import TfBool
from terraform_model.types.primitives.tfnumber import TfNumber
from terraform_model.types.internal.tfunknown import tfunknown, TfUnknown
from terraform_model.types.conversions.typify import typify
from terraform_model.expressions.expression import Expression
from terraform_model.utils.errors import TerraformTypeError


class UnaryExpression(Expression):

    def __init__(self, op, right):
        right = typify(right)
        super().__init__(op, right)

    def __str__(self):
        return f'({self.op}{self.right})'

    @property
    def op(self):
        return self._args[0].data

    @property
    def right(self):
        return self._args[1]


def unary(op, right) -> Union[TfBool, TfNumber, TfUnknown]:
    u = UnaryExpression(op, right)
    if isinstance(u.right, TfBool):
        return u.to_bool()
    elif isinstance(u.right, TfNumber):
        return u.to_number()
    elif conf.strict_typing:
        raise TerraformTypeError(f'Unary expression expects bool or number. Received {repr(u.right)}')
    else:
        return u.to_unknown()
