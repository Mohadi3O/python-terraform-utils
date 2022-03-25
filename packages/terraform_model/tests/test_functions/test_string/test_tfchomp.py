# std
import unittest

# internal
from terraform_model.all import *


class TestTfChomp(unittest.TestCase):

    def test_tfchomp_type(self):
        x = variable('x', type=TfString)
        result = tfchomp(x)
        self.assertIsInstance(result, TfString)

    def test_tfchomp_str(self):
        x = variable('x', type=TfString)
        result = str(tfchomp(x))
        self.assertEqual(result, 'chomp(var.x)')
