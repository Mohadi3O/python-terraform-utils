# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import TfUnknown


class TestTfRegexall(unittest.TestCase):

    def test_tfregexall_type(self):
        x = variable('x', type=TfString)
        result = tfregexall('[a-z]+', x)
        self.assertIsInstance(result, TfList)

    def test_tfregexall_str(self):
        x = variable('x', type=TfString)
        result = str(tfregexall('[a-z]+', x))
        self.assertEqual(result, 'regexall("[a-z]+", var.x)')
