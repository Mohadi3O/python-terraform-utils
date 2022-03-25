# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfMerge(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfMap[TfNumber])
        y = variable('y', type=TfMap[TfNumber])
        result = tfmerge(x, y)
        self.assertIsInstance(result, TfMap)

    def test_element_type(self):
        x = variable('x', type=TfMap[TfNumber])
        y = variable('y', type=TfMap[TfNumber])
        result = tfmerge(x, y).element_type()
        self.assertIs(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfMap[TfNumber])
        y = variable('y', type=TfMap[TfNumber])
        result = str(tfmerge(x, y))
        self.assertEqual(result, 'merge(var.x, var.y)')

    def test_non_similar_element_types(self):
        x = variable('x', type=TfMap[TfNumber])
        y = variable('y', type=TfMap[TfString])
        with self.assertRaises(TerraformTypeError):
            _ = tfmerge(x, y)
