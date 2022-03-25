# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.internal import tfassert
from terraform_model.utils.errors import TerraformTypeError


class TestTfIndex(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfString)
        result = tfindex(x, y)
        self.assertIsInstance(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfString)
        result = str(tfindex(x, y))
        self.assertEqual(result, 'index(var.x, var.y)')

    def test_unknown_element_type(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfString)
        with self.assertRaises(TerraformTypeError):
            _ = tfindex(x, y)

    def test_element_type_mismatch(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        with self.assertRaises(TerraformTypeError):
            _ = tfindex(x, y)
