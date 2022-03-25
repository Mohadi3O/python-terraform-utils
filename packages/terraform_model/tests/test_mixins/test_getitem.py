# std
import types
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import *


class TestGetItem(unittest.TestCase):

    def test_getitem_map_type(self):
        v = variable('x', type=TfMap)
        result = v['y']
        self.assertIsInstance(result, TfUnknown)

    def test_getitem_map_getitem_type(self):
        v = variable('x', type=TfMap)
        result = v['y']['z']
        self.assertIsInstance(result, TfUnknown)
