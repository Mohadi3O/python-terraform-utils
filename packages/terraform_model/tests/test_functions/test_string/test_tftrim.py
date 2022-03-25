# std
import unittest

# internal
from terraform_model.all import *


class TestTfTrim(unittest.TestCase):

    def test_tftrim_type(self):
        x = variable('x', type=TfString)
        result = tftrim(x)
        self.assertIsInstance(result, TfString)

    def test_tftrim_str(self):
        x = variable('x', type=TfString)
        result = str(tftrim(x))
        self.assertEqual(result, 'trim(var.x, " ")')
