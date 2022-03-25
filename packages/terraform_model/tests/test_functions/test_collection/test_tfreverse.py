# std
import unittest

# internal
from terraform_model.all import *


class TestTfReverse(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList[TfString])
        result = tfreverse(x)
        self.assertIsInstance(result, TfList)

    def test_element_type(self):
        x = variable('x', type=TfList[TfString])
        result = tfreverse(x).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfList[TfString])
        result = str(tfreverse(x))
        self.assertEqual(result, 'reverse(var.x)')
