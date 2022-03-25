# std
import unittest

# internal
from terraform_model.all import *


class TestTfSigNum(unittest.TestCase):

    def test_tfsignum_type(self):
        x = variable('x', type=TfNumber)
        result = tfsignum(x)
        self.assertIsInstance(result, TfNumber)

    def test_tfsignum_str(self):
        x = variable('x', type=TfNumber)
        result = str(tfsignum(x))
        self.assertEqual(result, 'signum(var.x)')
