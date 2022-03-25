# std
import unittest

# internal
from terraform_model.all import *


class TestTfFormatList(unittest.TestCase):

    def test_tfformatlist_type(self):
        x = variable('x', type=TfList)
        result = tfformatlist('Hello, %s!', x)
        self.assertIsInstance(result, TfList)

    def test_tfformatlist_str(self):
        x = variable('x', type=TfString)
        y = variable('y', type=TfList)
        result = str(tfformatlist('Hello, %s!', x, y))
        self.assertEqual(result, 'formatlist("Hello, %s!", var.x, var.y)')
