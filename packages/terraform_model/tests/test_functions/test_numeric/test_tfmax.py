# std
import unittest

# internal
from terraform_model.all import *


class TestTfMax(unittest.TestCase):

    def test_tfmax_type(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = tfmax(x, y)
        self.assertIsInstance(result, TfNumber)

    def test_tfmax_str(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = str(tfmax(x, y))
        self.assertEqual(result, 'max(var.x, var.y)')
