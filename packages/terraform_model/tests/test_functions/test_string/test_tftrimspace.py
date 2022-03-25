# std
import unittest

# internal
from terraform_model.all import *


class TestTfTrimSpace(unittest.TestCase):

    def test_tftrimspace_type(self):
        x = variable('x', type=TfString)
        result = tftrimspace(x)
        self.assertIsInstance(result, TfString)

    def test_tftrimspace_str(self):
        x = variable('x', type=TfString)
        result = str(tftrimspace(x))
        self.assertEqual(result, 'trimspace(var.x)')
