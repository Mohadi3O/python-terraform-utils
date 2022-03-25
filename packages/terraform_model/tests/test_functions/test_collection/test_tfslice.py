# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfSlice(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfNumber)
        result = tfslice(x, y, z)
        self.assertIsInstance(result, TfList)

    def test_element_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfNumber)
        result = tfslice(x, y, z).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfNumber)
        result = str(tfslice(x, y, z))
        self.assertEqual(result, 'slice(var.x, var.y, var.z)')

    def test_no_indices(self):
        x = variable('x', type=TfList[TfString])
        result = str(tfslice(x))
        self.assertEqual(result, 'slice(var.x, 0, length(var.x))')

    def test_start_index_only(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        result = str(tfslice(x, start_index=y))
        self.assertEqual(result, 'slice(var.x, var.y, length(var.x))')

    def test_end_index_only(self):
        x = variable('x', type=TfList[TfString])
        z = variable('z', type=TfNumber)
        result = str(tfslice(x, end_index=z))
        self.assertEqual(result, 'slice(var.x, 0, var.z)')
