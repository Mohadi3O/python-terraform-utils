# std
import unittest

# internal
from terraform_model.all import *


class TestTfTitle(unittest.TestCase):

    def test_tftitle_type(self):
        x = variable('x', type=TfString)
        result = tftitle(x)
        self.assertIsInstance(result, TfString)

    def test_tftitle_str(self):
        x = variable('x', type=TfString)
        result = str(tftitle(x))
        self.assertEqual(result, 'title(var.x)')
