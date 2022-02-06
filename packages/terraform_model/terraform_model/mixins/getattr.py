# internal
from terraform_model.utils.deferred import deferred


class GetAttrMixin:

    def __getattr__(self, attr):
        if attr in dir(self):
            return getattr(self, attr)
        else:
            return deferred.GetAttr(self, attr)
