# std
import types
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import *


class TestGetItem(unittest.TestCase):

    def test_tfunknown_to_bool(self):
        x = tfunknown()
        result = x.to_bool()
        self.assertIsInstance(result, TfBool)

    def test_tfunknown_to_null(self):
        x = tfunknown()
        result = x.to_null()
        self.assertIsInstance(result, TfNull)

    def test_tfunknown_to_number(self):
        x = tfunknown()
        result = x.to_number()
        self.assertIsInstance(result, TfNumber)

    def test_tfunknown_to_string(self):
        x = tfunknown()
        result = x.to_string()
        self.assertIsInstance(result, TfString)

    def test_tfunknown_to_list(self):
        x = tfunknown()
        result = x.to_list()
        self.assertIsInstance(result, TfList)

    def test_tfunknown_to_map(self):
        x = tfunknown()
        result = x.to_map()
        self.assertIsInstance(result, TfMap)

    def test_tfunknown_to_unknown(self):
        x = tfunknown()
        result = x.to_unknown()
        self.assertIsInstance(result, TfUnknown)

    def test_tfunknown_to_any(self):
        x = tfunknown()
        result = x.to_any()
        self.assertIsInstance(result, TfAny)
