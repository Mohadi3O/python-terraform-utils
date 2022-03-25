# std
import unittest

# internal
from terraform_model.all import *


class TestTfFormat(unittest.TestCase):

    def test_tfformat_type(self):
        x = variable('x', type=TfString)
        result = tfformat('Hello, %s!', x)
        self.assertIsInstance(result, TfString)

    def test_tfformat_str(self):
        x = variable('x', type=TfString)
        result = str(tfformat('Hello, %s!', x))
        self.assertEqual(result, 'format("Hello, %s!", var.x)')
