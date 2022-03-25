# std
import unittest

# internal
from terraform_model.all import *


class TestTfSplit(unittest.TestCase):

    def test_tfsplit_type(self):
        x = variable('x', type=TfString)
        result = tfsplit(',', x)
        self.assertIsInstance(result, TfList)

    def test_tfsplit_str(self):
        x = variable('x', type=TfString)
        result = str(tfsplit(',', x))
        self.assertEqual(result, 'split(",", var.x)')
