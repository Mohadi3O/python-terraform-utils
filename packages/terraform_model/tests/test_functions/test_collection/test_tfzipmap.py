# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfZipMap(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfNumber])
        result = tfzipmap(x, y)
        self.assertIsInstance(result, TfMap)

    def test_element_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfNumber])
        result = tfzipmap(x, y).element_type()
        self.assertIs(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfNumber])
        result = str(tfzipmap(x, y))
        self.assertEqual(result, 'zipmap(var.x, var.y)')

    def test_bad_keyslist_type(self):
        x = variable('x', type=TfMap[TfString])
        y = variable('y', type=TfList[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tfzipmap(x, y)

    def test_bad_keyslist_element_type(self):
        x = variable('x', type=TfList[TfNumber])
        y = variable('y', type=TfList[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tfzipmap(x, y)

    def test_bad_valueslist_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfMap[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tfzipmap(x, y)
