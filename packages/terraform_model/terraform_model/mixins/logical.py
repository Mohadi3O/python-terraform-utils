# std
from __future__ import annotations

# internal
from terraform_model.internal.deferred import deferred


class LogicalMixin:

    def __and__(self, other: LogicalMixin):
        return deferred.logical(self, '&&', other)

    def __or__(self, other: LogicalMixin):
        return deferred.logical(self, '||', other)

    def __invert__(self):
        return deferred.unary('!', self)
