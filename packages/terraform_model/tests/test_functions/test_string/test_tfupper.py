# std
import unittest

# internal
from terraform_model.all import *


class TestTfUpper(unittest.TestCase):

    def test_tfupper_type(self):
        x = variable('x', type=TfString)
        result = tfupper(x)
        self.assertIsInstance(result, TfString)

    def test_tfupper_str(self):
        x = variable('x', type=TfString)
        result = str(tfupper(x))
        self.assertEqual(result, 'upper(var.x)')
