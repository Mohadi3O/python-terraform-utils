# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.primitives import *
from terraform_model.utils.errors import TerraformTypeError


class TestLogical(unittest.TestCase):

    def test_logical_bools_type(self):
        x = TfBool(True)
        y = TfBool(False)
        result = x & y
        self.assertIsInstance(result, TfBool)

    def test_logical_not_bools_raises(self):
        x = TfBool(True)
        y = TfString('false')
        with self.assertRaises(TerraformTypeError):
            _ = x & y

    def test_logical_and(self):
        x = TfBool(True)
        y = TfBool(False)
        result = str(x & y)
        self.assertEqual(result, '(true && false)')

    def test_logical_or(self):
        x = TfBool(variable('x'))
        y = TfBool(variable('y'))
        result = str(x | y)
        self.assertEqual(result, '(var.x || var.y)')

    def test_logical_not(self):
        x = TfBool(variable('x'))
        result = str(~x)
        self.assertEqual(result, '(!var.x)')
