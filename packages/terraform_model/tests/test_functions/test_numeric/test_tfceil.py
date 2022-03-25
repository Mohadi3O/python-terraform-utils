# std
import unittest

# internal
from terraform_model.all import *


class TestTfCeil(unittest.TestCase):

    def test_tfceil_type(self):
        x = variable('x', type=TfNumber)
        result = tfceil(x)
        self.assertIsInstance(result, TfNumber)

    def test_tfceil_str(self):
        x = variable('x', type=TfNumber)
        result = str(tfceil(x))
        self.assertEqual(result, 'ceil(var.x)')
