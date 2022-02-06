from terraform_model.expressions.expression import Expression


class GetAttr(Expression):

    def __init__(self, obj, attr):
        super().__init__(obj, attr)

    def __str__(self):
        return f'{self.obj}.{self.attr}'

    @property
    def obj(self):
        return self._args[0]

    @property
    def attr(self):
        return self._args[1]
