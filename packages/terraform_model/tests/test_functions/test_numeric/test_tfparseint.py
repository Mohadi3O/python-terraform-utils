# std
import unittest

# internal
from terraform_model.all import *


class TestTfParseInt(unittest.TestCase):

    def test_tfparseint_type(self):
        x = variable('x', type=TfString)
        result = tfparseint(x)
        self.assertIsInstance(result, TfNumber)

    def test_tfparseint_str_default_base(self):
        x = variable('x', type=TfString)
        result = str(tfparseint(x))
        self.assertEqual(result, 'parseint(var.x, 10)')

    def test_tfparseint_str_nondefault_base_int(self):
        x = variable('x', type=TfString)
        result = str(tfparseint(x, 2))
        self.assertEqual(result, 'parseint(var.x, 2)')

    def test_tfparseint_str_nondefault_base_TfNumber(self):
        x = variable('x', type=TfString)
        y = variable('y', type=TfNumber)
        result = str(tfparseint(x, y))
        self.assertEqual(result, 'parseint(var.x, var.y)')
