# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfSort(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList[TfString])
        result = tfsort(x)
        self.assertIsInstance(result, TfList)

    def test_element_type(self):
        x = variable('x', type=TfList[TfString])
        result = tfsort(x).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfList[TfString])
        result = str(tfsort(x))
        self.assertEqual(result, 'sort(var.x)')

    def test_bad_type(self):
        x = variable('x', type=TfSet[TfString])
        with self.assertRaises(TerraformTypeError):
            _ = tfsort(x)

    def test_bad_element_type(self):
        x = variable('x', type=TfList[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tfsort(x)
