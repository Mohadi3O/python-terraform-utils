# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTernary(unittest.TestCase):

    def test_ternary_type(self):
        x = variable('x', type=TfBool)
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfNumber)
        result = ternary(x, y, z)
        self.assertIsInstance(result, TfNumber)

    def test_ternary_str(self):
        x = variable('x', type=TfBool)
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfNumber)
        result = str(ternary(x, y, z))
        self.assertEqual(result, '(var.x ? var.y : var.z)')

    def test_ternary_type_mismatch(self):
        x = variable('x', type=TfBool)
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfString)
        with self.assertRaises(TerraformTypeError):
            _ = ternary(x, y, z)
