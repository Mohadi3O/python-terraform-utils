from terraform_model.types.collections.collection import Collection
from terraform_model.utils.json import dumps
from terraform_model.mixins.literal import LiteralMixin


class List(Collection):

    def __str__(self) -> str:
        if isinstance(self.data, list):
            return dumps(self.data)
        else:
            return str(self.data)


class ListLiteral(List, LiteralMixin):

    def __init__(self, data: list):
        super().__init__(data)
