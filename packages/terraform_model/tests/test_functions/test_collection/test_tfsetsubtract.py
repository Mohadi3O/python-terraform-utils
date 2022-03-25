# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfSetSubtract(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfSet)
        result = tfsetsubtract(x, y)
        self.assertIsInstance(result, TfSet)

    def test_element_type(self):
        x = variable('x', type=TfSet[TfString])
        y = variable('y', type=TfSet[TfString])
        result = tfsetsubtract(x, y).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfSet)
        result = str(tfsetsubtract(x, y))
        self.assertEqual(result, 'setsubtract(var.x, var.y)')

    def test_mixed_element_types(self):
        x = variable('x', type=TfSet[TfNumber])
        y = variable('y', type=TfSet[TfString])
        with self.assertRaises(TerraformTypeError):
            _ = tfsetsubtract(x, y)
