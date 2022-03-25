# std
import unittest

# internal
from terraform_model.all import *


class TestTfTrimPrefix(unittest.TestCase):

    def test_tftrimprefix_type(self):
        x = variable('x', type=TfString)
        result = tftrimprefix(x, '!!')
        self.assertIsInstance(result, TfString)

    def test_tftrimprefix_str(self):
        x = variable('x', type=TfString)
        result = str(tftrimprefix(x, '!!'))
        self.assertEqual(result, 'trimprefix(var.x, "!!")')
