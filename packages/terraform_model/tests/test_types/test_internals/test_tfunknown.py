# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import *
from terraform_model.utils.conf import StrictTyping


class TestTfUnknown(unittest.TestCase):

    def test_tfunknown_loose(self):
        with StrictTyping(False):
            result = tfunknown()
            self.assertIsInstance(result, TfUnknownLoose)

    def test_tfunknown_loose_getattr(self):
        with StrictTyping(False):
            result = tfunknown(variable('x')).y
            self.assertIsInstance(result, TfUnknownLoose)

    def test_tfunknown_strict(self):
        with StrictTyping(True):
            result = tfunknown()
            self.assertIsInstance(result, TfUnknownStrict)

    def test_tfunknown_strict_getattr(self):
        with StrictTyping(True):
            with self.assertRaises(AttributeError):
                _ = tfunknown(variable('x')).y
