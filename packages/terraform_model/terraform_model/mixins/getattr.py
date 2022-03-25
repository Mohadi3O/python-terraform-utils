# internal
from terraform_model.internal.deferred import deferred


class GetAttrMixin:

    def __getattr__(self, attr):
        return deferred.typify(deferred.GetAttr(self, attr))
