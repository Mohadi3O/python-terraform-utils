# std
import unittest

# internal
from terraform_model.all import *


class TestTfTrimSuffix(unittest.TestCase):

    def test_tftrimsuffix_type(self):
        x = variable('x', type=TfString)
        result = tftrimsuffix(x, '!!')
        self.assertIsInstance(result, TfString)

    def test_tftrimsuffix_str(self):
        x = variable('x', type=TfString)
        result = str(tftrimsuffix(x, '!!'))
        self.assertEqual(result, 'trimsuffix(var.x, "!!")')
