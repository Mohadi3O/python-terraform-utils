# internal
from terraform_model.internal.deferred import deferred


class ContainsMixin:

    def contains(self, item):
        return deferred.tfcontains(self, item)
