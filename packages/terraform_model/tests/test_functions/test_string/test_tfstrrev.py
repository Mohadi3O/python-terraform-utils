# std
import unittest

# internal
from terraform_model.all import *


class TestTfStrRev(unittest.TestCase):

    def test_tfstrrev_type(self):
        x = variable('x', type=TfString)
        result = tfstrrev(x)
        self.assertIsInstance(result, TfString)

    def test_tfstrrev_str(self):
        x = variable('x', type=TfString)
        result = str(tfstrrev(x))
        self.assertEqual(result, 'strrev(var.x)')
