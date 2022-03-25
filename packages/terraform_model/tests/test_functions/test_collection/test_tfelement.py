# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import *


class TestTfElement(unittest.TestCase):

    def test_type_unknown(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfNumber)
        result = tfelement(x, y)
        self.assertIsInstance(result, TfUnknown)

    def test_type_known_from_variable_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        result = tfelement(x, y)
        self.assertIsInstance(result, TfString)

    def test_type_known(self):
        x = [1, 2, 3]
        y = variable('y', type=TfNumber)
        result = tfelement(x, y)
        self.assertIsInstance(result, TfNumber)

    def test_str(self):
        x = variable('x', type=TfList)
        y = variable('y', type=TfNumber)
        result = str(tfelement(x, y))
        self.assertEqual(result, 'element(var.x, var.y)')
