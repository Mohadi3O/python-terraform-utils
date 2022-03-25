# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfValues(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfMap[TfNumber])
        result = tfvalues(x)
        self.assertIsInstance(result, TfList)

    def test_element_type(self):
        x = variable('x', type=TfMap[TfNumber])
        result = tfvalues(x).element_type()
        self.assertIs(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfMap)
        result = str(tfvalues(x))
        self.assertEqual(result, 'values(var.x)')

    def test_bad_type(self):
        x = variable('x', type=TfList)
        with self.assertRaises(TerraformTypeError):
            _ = str(tfvalues(x))
