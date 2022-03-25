# std
import unittest

# internal
from terraform_model.blocks import data

# testing
from terraform_model.helpers.scope import Scope


class TestData(unittest.TestCase):

    def tearDown(self) -> None:
        Scope.clear_scopes()

    def test_str(self):
        d = data('x', 'y')
        self.assertEqual(str(d), 'data.x.y')

    def test_repr(self):
        d = data('x', 'y')
        self.assertEqual(repr(d), '<unknown> data.x.y')

    def test_expression(self):
        d = data('x', 'y')
        self.assertEqual(d.expression(), '${data.x.y}')
