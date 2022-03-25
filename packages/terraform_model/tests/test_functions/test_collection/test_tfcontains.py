# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.internal import tfassert
from terraform_model.utils.errors import TerraformTypeError


class TestTfContains(unittest.TestCase):

    def test_tflist(self):
        x = variable('x', type=TfList[TfNumber])
        y = variable('y', type=TfNumber)
        result = tfcontains(x, y)
        tfassert.is_instance(result, TfBool)

    def test_tfset(self):
        x = variable('x', type=TfSet[TfNumber])
        y = variable('y', type=TfNumber)
        result = tfcontains(x, y)
        tfassert.is_instance(result, TfBool)

    def test_str(self):
        x = variable('x', type=TfList[TfNumber])
        y = variable('y', type=TfNumber)
        result = str(tfcontains(x, y))
        self.assertEqual(result, 'contains(var.x, var.y)')

    def test_bad_type(self):
        x = variable('x', type=TfMap)
        y = variable('y', type=TfNumber)
        with self.assertRaises(TerraformTypeError):
            _ = tfcontains(x, y)

    def test_element_type_mismatch(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        with self.assertRaises(TerraformTypeError):
            _ = tfcontains(x, y)
