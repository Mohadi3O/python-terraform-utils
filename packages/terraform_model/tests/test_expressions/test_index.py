# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestIndex(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        result = x[y]
        self.assertIsInstance(result, TfString)

    def test_str(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        result = str(x[y])
        self.assertEqual(result, 'var.x[var.y]')

    def test_type_mismatch(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfString)
        with self.assertRaises(TerraformTypeError):
            _ = x[y]
