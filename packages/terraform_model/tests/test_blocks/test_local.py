# std
import unittest

# internal
from terraform_model.blocks import local

# testing
from terraform_model.helpers.scope import Scope


class TestLocal(unittest.TestCase):

    def tearDown(self) -> None:
        Scope.clear_scopes()

    def test_str(self):
        l = local('x', 'val')
        self.assertEqual(str(l), 'local.x')

    def test_repr(self):
        l = local('x', 'val')
        self.assertEqual(repr(l), '<string> local.x')

    def test_expression(self):
        l = local('x', 'val')
        self.assertEqual(l.expression(), '${local.x}')
