# internal
from terraform_model.internal.deferred import deferred


class LengthMixin:

    def __len__(self):
        return self.length()

    def length(self):
        return deferred.tflength(self)
