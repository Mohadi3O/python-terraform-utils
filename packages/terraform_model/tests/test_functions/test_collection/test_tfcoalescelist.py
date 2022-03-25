# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.internal import tfassert
from terraform_model.utils.errors import TerraformTypeError


class TestTfCoalesceList(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfList)
        result = tfcoalescelist(x, y)
        tfassert.is_instance(result, TfList)

    def test_type_with_element_type(self):
        x = variable('x', type=TfList[TfNumber])
        y = variable('y', type=TfList[TfNumber])
        result = tfcoalescelist(x, y)
        tfassert.is_instance(result, TfList[TfNumber])

    def test_str(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfList)
        result = str(tfcoalescelist(x, y))
        self.assertEqual(result, 'coalescelist(var.x, var.y)')

    def test_type_mismatch(self):
        x = variable('x', type=TfList[TfNumber])
        y = variable('y', type=TfSet[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tfcoalescelist(x, y)

    def test_element_type_mismatch(self):
        x = variable('x', type=TfList[TfNumber])
        y = variable('y', type=TfList[TfString])
        with self.assertRaises(TerraformTypeError):
            _ = tfcoalescelist(x, y)
