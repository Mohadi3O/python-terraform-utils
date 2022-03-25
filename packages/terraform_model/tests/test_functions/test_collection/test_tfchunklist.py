# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.internal import tfassert
from terraform_model.internal.tftype import tftype
from terraform_model.utils.errors import TerraformTypeError


class TestTfChunkList(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList)
        result = tfchunklist(x, 2)
        self.assertIsInstance(result, TfList)

    def test_element_type_shallow(self):
        x = variable('x', type=TfList[TfString])
        result = tfchunklist(x, 2).element_type()
        tfassert.is_instance(result, TfList)

    def test_element_type_deep(self):
        x = variable('x', type=TfList[TfString])
        result = tfchunklist(x, 2).element_type(deep=True)
        tfassert.is_instance(result, TfList[TfString])

    def test_tftype_shallow(self):
        x = variable('x', type=TfList[TfString])
        result = tftype(tfchunklist(x, 2))
        tfassert.is_instance(result, TfList)

    def test_tftype_deep(self):
        x = variable('x', type=TfList[TfString])
        result = tftype(tfchunklist(x, 2), deep=True)
        tfassert.is_instance(result, TfList[TfList[TfString]])

    def test_str(self):
        x = variable('x', type=TfList)
        result = str(tfchunklist(x, 2))
        self.assertEqual(result, 'chunklist(var.x, 2)')

    def test_bad_type(self):
        x = variable('x', type=TfMap)
        with self.assertRaises(TerraformTypeError):
            _ = tfchunklist(x, 2)
