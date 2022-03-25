# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfCoalesce(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = tfcoalesce(x, y)
        self.assertIsInstance(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = str(tfcoalesce(x, y))
        self.assertEqual(result, 'coalesce(var.x, var.y)')

    def test_type_mismatch(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfString)
        with self.assertRaises(TerraformTypeError):
            _ = tfcoalesce(x, y)
