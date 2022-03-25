# std
import unittest

# internal
from terraform_model.blocks import variable

# testing
from terraform_model.helpers.scope import Scope


class TestScope(unittest.TestCase):

    def tearDown(self) -> None:
        Scope.clear_scopes()

    def test_something(self):
        variable('x')
        Scope.get_scope().get_items()
