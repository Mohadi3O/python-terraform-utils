# std
import types
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import *


class TestGetItem(unittest.TestCase):

    def test_tfany_getattr_type(self):
        x = variable('x', type=TfAny)
        result = x.y
        self.assertIsInstance(result, TfUnknown)

    def test_tfany_getattr_str(self):
        x = variable('x', type=TfAny)
        result = str(x.y)
        self.assertEqual(result, 'var.x.y')
