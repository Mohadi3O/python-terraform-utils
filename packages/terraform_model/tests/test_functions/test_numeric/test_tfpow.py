# std
import unittest

# internal
from terraform_model.all import *


class TestTfPow(unittest.TestCase):

    def test_tfpow_type(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = tfpow(x, y)
        self.assertIsInstance(result, TfNumber)

    def test_tfpow_str(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = str(tfpow(x, y))
        self.assertEqual(result, 'pow(var.x, var.y)')
