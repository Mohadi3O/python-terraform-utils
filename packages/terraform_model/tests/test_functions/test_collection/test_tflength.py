# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfLength(unittest.TestCase):

    def test_type_string(self):
        x = variable('x', type=TfString)
        result = tflength(x)
        self.assertIsInstance(result, TfNumber)

    def test_type_list(self):
        x = variable('x', type=TfList)
        result = tflength(x)
        self.assertIsInstance(result, TfNumber)

    def test_type_map(self):
        x = variable('x', type=TfMap)
        result = tflength(x)
        self.assertIsInstance(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfString)
        result = str(tflength(x))
        self.assertEqual(result, 'length(var.x)')

    def test_bad_input_type(self):
        x = variable('x', type=TfNull)
        with self.assertRaises(TerraformTypeError):
            _ = tflength(x)
