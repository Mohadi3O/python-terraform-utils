# internal
from terraform_model.internal.deferred import deferred


class ToMixin:

    def to_bool(self):
        return deferred.tfbool(self)

    def to_null(self):
        return deferred.tfnull(self)

    def to_number(self):
        return deferred.tfnumber(self)

    def to_string(self):
        return deferred.tfstring(self)

    def to_list(self):
        return deferred.tflist(self)

    def to_map(self):
        return deferred.tfmap(self)

    def to_unknown(self):
        return deferred.tfunknown(self)

    def to_any(self):
        return deferred.tfany(self)
