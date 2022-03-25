# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfAnyTrue(unittest.TestCase):

    def test_type_tfbool(self):
        x = variable('x', type=TfList[TfBool])
        result = tfanytrue(x)
        self.assertIsInstance(result, TfBool)

    def test_type_tfstring(self):
        x = variable('x', type=TfList[TfString])
        result = tfanytrue(x)
        self.assertIsInstance(result, TfBool)

    def test_str(self):
        l = [True, False]
        result = str(tfanytrue(l))
        self.assertEqual(result, 'anytrue([\n  true,\n  false\n])')

    def test_bad_type(self):
        x = variable('x', type=TfMap)
        with self.assertRaises(TerraformTypeError):
            _ = tfanytrue(x)

    def test_bad_element_type(self):
        x = variable('x', type=TfList[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tfanytrue(x)
