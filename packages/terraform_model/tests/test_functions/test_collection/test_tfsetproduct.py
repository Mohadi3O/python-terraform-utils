# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfSetProduct(unittest.TestCase):

    def test_type_set(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfSet)
        result = tfsetproduct(x, y)
        self.assertIsInstance(result, TfSet)

    def test_type_list(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfList)
        result = tfsetproduct(x, y)
        self.assertIsInstance(result, TfList)

    def test_element_type(self):
        x = variable('x', type=TfSet[TfString])
        y = variable('y', type=TfSet[TfString])
        result = tfsetproduct(x, y).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfSet)
        result = str(tfsetproduct(x, y))
        self.assertEqual(result, 'setproduct(var.x, var.y)')

    def test_many(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfSet)
        z = variable('z', type=TfSet)
        result = str(tfsetproduct(x, y, z))
        self.assertEqual(result, 'setproduct(var.x, var.y, var.z)')

    def test_mixed_sets_and_lists(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfList)
        with self.assertRaises(TerraformTypeError):
            _ = tfsetproduct(x, y)

    def test_mixed_element_types(self):
        x = variable('x', type=TfSet[TfNumber])
        y = variable('y', type=TfSet[TfString])
        with self.assertRaises(TerraformTypeError):
            _ = tfsetproduct(x, y)
