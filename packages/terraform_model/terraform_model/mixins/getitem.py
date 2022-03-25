# internal
from terraform_model.internal.deferred import deferred


class GetItemMixin:

    def __getitem__(self, item):
        return deferred.typify(deferred.GetItem(self, item))
