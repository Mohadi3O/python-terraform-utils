# std
import unittest

# internal
from terraform_model.all import *


class TestTfAbs(unittest.TestCase):

    def test_tfabs_type(self):
        x = variable('x', type=TfNumber)
        result = tfabs(x)
        self.assertIsInstance(result, TfNumber)

    def test_tfabs_str(self):
        x = variable('x', type=TfNumber)
        result = str(tfabs(x))
        self.assertEqual(result, 'abs(var.x)')
