from terraform_model.types.atomics.atomic import Atomic
from terraform_model.mixins.literal import LiteralMixin


class Bool(Atomic):

    def __str__(self):
        if isinstance(self.data, bool):
            return 'true' if self.data else 'false'
        else:
            return str(self.data)

    @classmethod
    def new(cls, data):
        if data is true or data is True:
            return true
        elif data is false or data is False:
            return false
        else:
            return Bool(data)


class BoolLiteral(Bool, LiteralMixin):

    def __init__(self, data: bool):
        super().__init__(data)

    def __str__(self):
        return 'true' if self.data else 'false'


true = BoolLiteral(True)
false = BoolLiteral(False)
