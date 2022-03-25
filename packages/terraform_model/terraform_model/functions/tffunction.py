# internal
from terraform_model.expressions.expression import Expression


class TfFunction(Expression):

    def __init__(self, name: str, *args):
        super().__init__(name, *args)

    def __str__(self):
        return f'{self.name}({", ".join(self.args)})'

    @property
    def name(self):
        return self._args[0].data

    @property
    def args(self):
        return self.strings()[1:]
