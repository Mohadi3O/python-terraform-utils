# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.primitives import *
from terraform_model.utils.errors import TerraformTypeError


class TestCompare(unittest.TestCase):

    def test_compare_numbers_type(self):
        x = TfNumber(1)
        y = TfNumber(2)
        result = x < y
        self.assertIsInstance(result, TfBool)

    def test_compare_not_numbers_raises(self):
        x = TfNumber(1)
        y = TfString('2')
        with self.assertRaises(TerraformTypeError):
            _ = x < y

    def test_compare_lt(self):
        x = TfNumber(1)
        y = TfNumber(2)
        result = str(x < y)
        self.assertEqual(result, '(1 < 2)')

    def test_compare_le(self):
        x = TfNumber(1)
        y = TfNumber(2)
        result = str(x <= y)
        self.assertEqual(result, '(1 <= 2)')

    def test_compare_eq(self):
        x = TfNumber(1)
        y = TfNumber(2)
        result = str(x == y)
        self.assertEqual(result, '(1 == 2)')

    def test_compare_ne(self):
        x = TfNumber(1)
        y = TfNumber(2)
        result = str(x != y)
        self.assertEqual(result, '(1 != 2)')

    def test_compare_gt(self):
        x = TfNumber(1)
        y = TfNumber(2)
        result = str(x > y)
        self.assertEqual(result, '(1 > 2)')

    def test_compare_ge(self):
        x = TfNumber(1)
        y = TfNumber(2)
        result = str(x >= y)
        self.assertEqual(result, '(1 >= 2)')
