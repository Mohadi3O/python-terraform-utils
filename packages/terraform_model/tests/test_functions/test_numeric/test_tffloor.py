# std
import unittest

# internal
from terraform_model.all import *


class TestTfFloor(unittest.TestCase):

    def test_tffloor_type(self):
        x = variable('x', type=TfNumber)
        result = tffloor(x)
        self.assertIsInstance(result, TfNumber)

    def test_tffloor_str(self):
        x = variable('x', type=TfNumber)
        result = str(tffloor(x))
        self.assertEqual(result, 'floor(var.x)')
