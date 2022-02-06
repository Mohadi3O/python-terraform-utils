from terraform_model.expressions.expression import Expression


class GetItem(Expression):

    def __init__(self, obj, item):
        super().__init__(obj, item)

    def __str__(self):
        return f'{self.obj}[{self.item}]'

    @property
    def obj(self):
        return self._args[0]

    @property
    def item(self):
        return self._args[1]
