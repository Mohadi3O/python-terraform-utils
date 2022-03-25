# std
import unittest

# internal
from terraform_model.all import *


class TestTfIndent(unittest.TestCase):

    def test_tfindent_type(self):
        x = variable('x', type=TfString)
        result = tfindent(2, x)
        self.assertIsInstance(result, TfString)

    def test_tfindent_str(self):
        x = variable('x', type=TfString)
        result = str(tfindent(2, x))
        self.assertEqual(result, 'indent(2, var.x)')
