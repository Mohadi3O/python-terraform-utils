from terraform_model.types.atomics.atomic import Atomic
from terraform_model.mixins.literal import LiteralMixin


class String(Atomic):

    def __str__(self):
        if isinstance(self.data, str):
            return self.data
        else:
            return str(self.data)


class StringLiteral(String, LiteralMixin):

    def __init__(self, data: str):
        super().__init__(data)

    def __str__(self):
        return self.data
