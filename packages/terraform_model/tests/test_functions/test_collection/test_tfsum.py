# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfSum(unittest.TestCase):

    def test_type_list(self):
        x = variable('x', type=TfList[TfNumber])
        result = tfsum(x)
        self.assertIsInstance(result, TfNumber)

    def test_type_set(self):
        x = variable('x', type=TfSet[TfNumber])
        result = tfsum(x)
        self.assertIsInstance(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfList[TfNumber])
        result = str(tfsum(x))
        self.assertEqual(result, 'sum(var.x)')

    def test_bad_type(self):
        x = variable('x', type=TfMap)
        with self.assertRaises(TerraformTypeError):
            _ = tfsum(x)

    def test_bad_element_type(self):
        x = variable('x', type=TfList[TfString])
        with self.assertRaises(TerraformTypeError):
            _ = tfsum(x)
