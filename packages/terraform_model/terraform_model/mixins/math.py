# std
from __future__ import annotations

# internal
from terraform_model.utils.deferred import deferred


class MathMixin:

    def __add__(self, other: MathMixin):
        return deferred.math(self, '+', other)

    def __sub__(self, other: MathMixin):
        return deferred.math(self, '-', other)

    def __mul__(self, other: MathMixin):
        return deferred.math(self, '*', other)

    def __truediv__(self, other: MathMixin):
        return deferred.math(self, '/', other)

    def __mod__(self, other: MathMixin):
        return deferred.math(self, '%', other)
