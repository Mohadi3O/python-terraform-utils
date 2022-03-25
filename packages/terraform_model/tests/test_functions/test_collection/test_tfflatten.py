# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfFlatten(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList)
        result = tfflatten(x)
        self.assertIsInstance(result, TfList)

    def test_str(self):
        x = variable('x', type=TfList)
        result = str(tfflatten(x))
        self.assertEqual(result, 'flatten(var.x)')

    def test_type_bad(self):
        x = variable('x', type=TfSet)
        with self.assertRaises(TerraformTypeError):
            _ = tfflatten(x)
