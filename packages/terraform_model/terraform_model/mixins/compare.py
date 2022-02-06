# std
from __future__ import annotations

# internal
from terraform_model.utils.deferred import deferred


class CompareMixin:

    def __lt__(self, other: CompareMixin):
        return deferred.compare(self, '<', other)

    def __le__(self, other: CompareMixin):
        return deferred.compare(self, '<=', other)

    def __eq__(self, other: CompareMixin):
        return deferred.compare(self, '==', other)

    def __ne__(self, other: CompareMixin):
        return deferred.compare(self, '!=', other)

    def __gt__(self, other: CompareMixin):
        return deferred.compare(self, '>', other)

    def __ge__(self, other: CompareMixin):
        return deferred.compare(self, '>=', other)
