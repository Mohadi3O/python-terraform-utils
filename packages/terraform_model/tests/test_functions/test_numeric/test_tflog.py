# std
import unittest

# internal
from terraform_model.all import *


class TestTfLog(unittest.TestCase):

    def test_tflog_type(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = tflog(x, y)
        self.assertIsInstance(result, TfNumber)

    def test_tflog_str(self):
        x = variable('x', type=TfNumber)
        y = variable('y', type=TfNumber)
        result = str(tflog(x, y))
        self.assertEqual(result, 'log(var.x, var.y)')
