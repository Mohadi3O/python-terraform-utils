# internal
from terraform_model.expressions.expression import Expression
from terraform_model.internal.deferred import deferred


class GetItem(Expression):

    def __init__(self, obj, item):
        super().__init__(deferred.typify(obj), deferred.typify(item))

    def __str__(self):
        return f'{self.obj}[{self.item}]'

    @property
    def obj(self):
        return self._args[0]

    @property
    def item(self):
        return self._args[1]
