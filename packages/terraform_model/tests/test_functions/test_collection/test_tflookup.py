# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfLookup(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfMap[TfNumber])
        result = tflookup(x, 'key', 1)
        self.assertIsInstance(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfMap[TfString])
        result = str(tflookup(x, 'abc', 'def'))
        self.assertEqual(result, 'lookup(var.x, "abc", "def")')

    def test_bad_map_type(self):
        m = variable('m', type=TfList)
        with self.assertRaises(TerraformTypeError):
            _ = tflookup(m, 'key', 1)

    def test_bad_key_type(self):
        m = variable('m', type=TfMap[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tflookup(m, 1, 2)

    def test_default_type_mismatch(self):
        m = variable('m', type=TfMap[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tflookup(m, 'key', 'asdf')
