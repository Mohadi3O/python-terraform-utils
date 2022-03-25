# internal
from tests.internal.base import BaseTestClass
from terraform_model.all import *
from terraform_model.internal import tfassert
from terraform_model.types.internal import TfUnknown
from terraform_model.utils.errors import TerraformTypeError


class TestTfConcat(BaseTestClass):

    def test_type(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfList)
        result = tfconcat(x, y)
        tfassert.is_instance(result, TfList[TfUnknown])

    def test_type_deep(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfString])
        result = tfconcat(x, y)
        tfassert.is_instance(result, TfList[TfString])

    def test_element_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfString])
        result = tfconcat(x, y).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfList)
        result = str(tfconcat(x, y))
        self.assertEqual(result, 'concat(var.x, var.y)')

    def test_non_matching_element_types(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfNumber])
        with self.assertRaises(TerraformTypeError):
            _ = tfconcat(x, y).element_type()

    def test__add__(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfList)
        result = str(x + y)
        self.assertEqual(result, 'concat(var.x, var.y)')
