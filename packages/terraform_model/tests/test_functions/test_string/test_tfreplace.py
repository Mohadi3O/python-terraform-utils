# std
import unittest

# internal
from terraform_model.all import *


class TestTfReplace(unittest.TestCase):

    def test_tfreplace_type(self):
        x = variable('x', type=TfString)
        result = tfreplace(x, '+', '-')
        self.assertIsInstance(result, TfString)

    def test_tfreplace_str(self):
        x = variable('x', type=TfString)
        result = str(tfreplace(x, '+', '-'))
        self.assertEqual(result, 'replace(var.x, "+", "-")')
