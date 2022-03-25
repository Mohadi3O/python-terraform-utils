# std
import unittest

# internal
from terraform_model.all import *


class TestTfMin(unittest.TestCase):

    def test_tfmin_type(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = tfmin(x, y)
        self.assertIsInstance(result, TfNumber)

    def test_tfmin_str(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = str(tfmin(x, y))
        self.assertEqual(result, 'min(var.x, var.y)')
