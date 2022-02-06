from terraform_model.types.atomics.atomic import Atomic
from terraform_model.mixins.literal import LiteralMixin


class Null(Atomic):

    def __init__(self, data):
        super().__init__(data)

    def __str__(self):
        return 'null'


class NullLiteral(Null, LiteralMixin):

    def __init__(self):
        super().__init__(None)


null = NullLiteral()
