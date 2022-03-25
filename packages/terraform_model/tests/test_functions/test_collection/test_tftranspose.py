# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError
from terraform_model.internal import tfassert


class TestTfTranspose(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfMap[TfList[TfString]])
        result = tftranspose(x)
        tfassert.is_instance(result, TfMap[TfList[TfString]])

    def test_str(self):
        x = variable('x', type=TfMap[TfList[TfString]])
        result = str(tftranspose(x))
        self.assertEqual(result, 'transpose(var.x)')

    def test_bad_type(self):
        x = variable('x', type=TfMap)
        with self.assertRaises(TerraformTypeError):
            _ = tftranspose(x)

    def test_bad_element_type(self):
        x = variable('x', type=TfMap[TfString])
        with self.assertRaises(TerraformTypeError):
            _ = tftranspose(x)
