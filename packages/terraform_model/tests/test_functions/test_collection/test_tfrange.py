# std
import unittest

# internal
from terraform_model.all import *


class TestTfRange(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfNumber)
        result = tfrange(x)
        self.assertIsInstance(result, TfList)

    def test_element_type(self):
        x = variable('x', type=TfNumber)
        result = tfrange(x).element_type()
        self.assertIs(result, TfNumber)

    def test_one_input_str(self):
        x = variable('x', type=TfNumber)
        result = str(tfrange(x))
        self.assertEqual(result, 'range(var.x)')

    def test_two_inputs_str(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = str(tfrange(x, y))
        self.assertEqual(result, 'range(var.x, var.y)')

    def test_three_inputs_str(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfNumber)
        result = str(tfrange(x, y, z))
        self.assertEqual(result, 'range(var.x, var.y, var.z)')
