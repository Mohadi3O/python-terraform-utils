# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.internal import tfassert
from terraform_model.utils.errors import TerraformTypeError


class TestTfDistinct(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList)
        result = tfdistinct(x)
        tfassert.is_instance(result, TfList)

    def test_type_deep(self):
        x = variable('x', type=TfList[TfString])
        result = tfdistinct(x)
        tfassert.is_instance(result, TfList[TfString])

    def test_str(self):
        x = variable('x', type=TfList)
        result = str(tfdistinct(x))
        self.assertEqual(result, 'distinct(var.x)')

    def test_not_list(self):
        x = variable('x', type=TfSet)
        with self.assertRaises(TerraformTypeError):
            _ = tfdistinct(x)
