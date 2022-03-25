# std
import unittest

# internal
from terraform_model.all import *


class TestTfLower(unittest.TestCase):

    def test_tflower_type(self):
        x = variable('x', type=TfString)
        result = tflower(x)
        self.assertIsInstance(result, TfString)

    def test_tflower_str(self):
        x = variable('x', type=TfString)
        result = str(tflower(x))
        self.assertEqual(result, 'lower(var.x)')
