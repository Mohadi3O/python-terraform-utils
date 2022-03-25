# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import TfUnknown


class TestTfOne(unittest.TestCase):

    def test_list_input(self):
        x = variable('x', type=TfList)
        result = tfone(x)
        self.assertIsInstance(result, TfUnknown)

    def test_tfstring(self):
        x = variable('x', type=TfList[TfString])
        result = tfone(x)
        self.assertIsInstance(result, TfString)

    def test_set_input(self):
        x = variable('x', type=TfSet)
        result = tfone(x)
        self.assertIsInstance(result, TfUnknown)

    def test_str(self):
        x = variable('x', type=TfList)
        result = str(tfone(x))
        self.assertEqual(result, 'one(var.x)')
