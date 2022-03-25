# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import *
from terraform_model.utils.errors import TerraformTypeError

# testing
from terraform_model.helpers.scope import Scope


class TestVariable(unittest.TestCase):

    def tearDown(self) -> None:
        Scope.clear_scopes()

    def test_str(self):
        v = variable('x')
        self.assertEqual(str(v), 'var.x')

    def test_repr(self):
        v = variable('x')
        self.assertEqual(repr(v), '<unknown> var.x')

    def test_expression(self):
        v = variable('x')
        self.assertEqual(v.expression(), '${var.x}')

    def test_add_numbers(self):
        z = variable('x', type=TfNumber) + variable('y', type=TfNumber)
        self.assertEqual(str(z), '(var.x + var.y)')

    def test_type_unknown(self):
        v = variable('x')
        self.assertIsInstance(v, TfUnknown)

    def test_type_number(self):
        v = variable('x', 1)
        self.assertIsInstance(v, TfNumber)

    def test_type_number_var_type(self):
        v = variable('x', type=TfNumber)
        self.assertIsInstance(v, TfNumber)

    def test_type_string(self):
        v = variable('x', 'abc')
        self.assertIsInstance(v, TfString)

    def test_type_string_var_type(self):
        v = variable('x', type=TfString)
        self.assertIsInstance(v, TfString)

    def test_type_bool(self):
        v = variable('x', True)
        self.assertIsInstance(v, TfBool)

    def test_type_bool_var_type(self):
        v = variable('x', type=TfBool)
        self.assertIsInstance(v, TfBool)

    def test_type_list(self):
        v = variable('x', [1, 2, 3])
        self.assertIsInstance(v, TfList)

    def test_type_list_var_type(self):
        v = variable('x', type=TfList)
        self.assertIsInstance(v, TfList)

    def test_list_element_type_from_default(self):
        v = variable('x', [1, 2, 3])
        result = v.element_type()
        self.assertIs(result, TfNumber)

    def test_list_element_type_from_type(self):
        v = variable('x', type=TfList[TfString])
        result = v.element_type()
        self.assertIs(result, TfString)

    def test_map_element_type_from_default(self):
        v = variable('x', {'x': 1, 'y': 2})
        result = v.element_type()
        self.assertIs(result, TfNumber)

    def test_map_element_type_from_type(self):
        v = variable('x', type=TfMap[TfString])
        result = v.element_type()
        self.assertIs(result, TfString)

    def test_type_map(self):
        v = variable('x', {'x': 1, 'y': 2})
        self.assertIsInstance(v, TfMap)

    def test_type_map_var_type(self):
        v = variable('x', type=TfMap)
        self.assertIsInstance(v, TfMap)

    def test_type_set(self):
        v = variable('x', {1, 2, 3})
        self.assertIsInstance(v, TfSet)

    def test_type_set_var_type(self):
        v = variable('x', type=TfSet)
        self.assertIsInstance(v, TfSet)

    def test_number_hashable(self):
        v = variable('x', type=TfNumber)
        result = hash(v)
        self.assertIsInstance(result, int)

    def test_string_hashable(self):
        v = variable('x', type=TfString)
        result = hash(v)
        self.assertIsInstance(result, int)

    def test_map_not_hashable(self):
        v = variable('x', type=TfMap)
        with self.assertRaises(TerraformTypeError):
            _ = hash(v)
