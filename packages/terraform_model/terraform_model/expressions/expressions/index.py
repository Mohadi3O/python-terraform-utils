# std
from typing import cast, Union

# internal
from terraform_model.expressions.expression import Expression
from terraform_model.internal.deferred import deferred
from terraform_model.types.collections.tflist import TfList
from terraform_model.types.primitives.tfnumber import TfNumber
from terraform_model.types.conversions.typify import typify
from terraform_model.internal import tfassert


class Index(Expression):

    def __init__(self, obj: TfList, index: TfNumber):
        tfassert.is_instance(obj, TfList)
        tfassert.is_instance(index, TfNumber)
        super().__init__(deferred.typify(obj), deferred.typify(index))

    def __str__(self):
        return f'{self.obj}[{self.index}]'

    @property
    def obj(self):
        return self._args[0]

    @property
    def index(self):
        return self._args[1]


def index(obj: TfList, index: Union[int, TfNumber]):
    index = cast(TfNumber, typify(index))
    return obj.element_type().new(Index(obj, index))
