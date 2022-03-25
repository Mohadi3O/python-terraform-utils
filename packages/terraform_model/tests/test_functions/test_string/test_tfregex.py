# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import TfUnknown


class TestTfRegex(unittest.TestCase):

    def test_tfregex_type(self):
        x = variable('x', type=TfString)
        result = tfregex('[a-z]+', x)
        self.assertIsInstance(result, TfUnknown)

    def test_tfregex_str(self):
        x = variable('x', type=TfString)
        result = str(tfregex('[a-z]+', x))
        self.assertEqual(result, 'regex("[a-z]+", var.x)')
