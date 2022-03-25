# std
import unittest

# internal
from terraform_model.blocks import output

# testing
from terraform_model.helpers.scope import Scope


class TestOutput(unittest.TestCase):

    def tearDown(self) -> None:
        Scope.clear_scopes()

    def test_str(self):
        o = output('x', 'val')
        self.assertEqual(str(o), '"val"')

    def test_repr(self):
        o = output('x', 'val')
        self.assertEqual(repr(o), '<string> "val"')

    def test_expression(self):
        o = output('x', 'val')
        self.assertEqual(o.expression(), '${"val"}')
