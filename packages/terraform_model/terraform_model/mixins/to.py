# internal
from terraform_model.utils.deferred import deferred


class ToMixin:

    def to_bool(self):
        return deferred.to_bool(self)

    def to_null(self):
        return deferred.to_null(self)

    def to_number(self):
        return deferred.to_number(self)

    def to_string(self):
        return deferred.to_string(self)

    def to_list(self):
        return deferred.to_list(self)

    def to_map(self):
        return deferred.to_map(self)
