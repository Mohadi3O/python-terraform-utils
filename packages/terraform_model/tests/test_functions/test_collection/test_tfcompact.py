# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.internal import tfassert
from terraform_model.utils.errors import TerraformTypeError


class TestTfCompact(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList[TfString])
        result = tfcompact(x)
        tfassert.is_instance(result, TfList[TfString])

    def test_element_type(self):
        x = variable('x', type=TfList[TfString])
        result = tfcompact(x)
        tfassert.element_type_is_instance(result, TfString)

    def test_str(self):
        x = variable('x', type=TfList[TfString])
        result = str(tfcompact(x))
        self.assertEqual(result, 'compact(var.x)')

    def test_type_unknown(self):
        x = variable('x', type=TfList)
        with self.assertRaises(TerraformTypeError):
            _ = tfcompact(x)

    def test_type_bad(self):
        x = variable('x', type=TfList[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tfcompact(x)
