# internal
from terraform_model.utils.deferred import deferred


class GetItemMixin:

    def __getitem__(self, item):
        return deferred.GetItem(self, item)
