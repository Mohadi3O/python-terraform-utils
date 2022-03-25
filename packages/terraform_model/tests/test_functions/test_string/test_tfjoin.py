# std
import unittest

# internal
from terraform_model.all import *


class TestTfJoin(unittest.TestCase):

    def test_tfjoin_type(self):
        x = variable('x', type=TfString)
        result = tfjoin(',', x)
        self.assertIsInstance(result, TfString)

    def test_tfjoin_str(self):
        x = variable('x', type=TfString)
        result = str(tfjoin(',', x))
        self.assertEqual(result, 'join(",", var.x)')
