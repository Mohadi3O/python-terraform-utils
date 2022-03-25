# std
import unittest

# internal
from terraform_model.all import *


class TestTfSubStr(unittest.TestCase):

    def test_tfsubstr_type(self):
        x = variable('x', type=TfString)
        result = tfsubstr(x, 1, 2)
        self.assertIsInstance(result, TfString)

    def test_tfsubstr_str(self):
        x = variable('x', type=TfString)
        result = str(tfsubstr(x, 1, 2))
        self.assertEqual(result, 'substr(var.x, 1, 2)')
