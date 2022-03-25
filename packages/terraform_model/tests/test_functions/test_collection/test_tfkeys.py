# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfKeys(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfMap)
        result = tfkeys(x)
        self.assertIsInstance(result, TfList)

    def test_element_type(self):
        x = variable('x', type=TfMap)
        result = tfkeys(x).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfMap)
        result = str(tfkeys(x))
        self.assertEqual(result, 'keys(var.x)')

    def test_bad_type(self):
        x = variable('x', type=TfList)
        with self.assertRaises(TerraformTypeError):
            _ = str(tfkeys(x))
