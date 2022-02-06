from terraform_model.types.collections.collection import Collection
from terraform_model.utils.json import dumps
from terraform_model.mixins.literal import LiteralMixin


class Map(Collection):

    def __str__(self) -> str:
        if isinstance(self.data, dict):
            return dumps(self.data)
        else:
            return str(self.data)


class MapLiteral(Map, LiteralMixin):

    def __init__(self, data: dict):
        super().__init__(data)
