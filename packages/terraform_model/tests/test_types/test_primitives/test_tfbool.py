# std
import unittest

# internal
from terraform_model.types.primitives.tfbool import tfbool, TfBool, TfBoolLiteral, true, false
from terraform_model.internal.tftype import tftype


class TestTfBool(unittest.TestCase):

    def test_bool_True(self):
        result = tfbool(True)
        self.assertIsInstance(result, TfBool)

    def test_bool_False(self):
        result = tfbool(False)
        self.assertIsInstance(result, TfBool)

    def test_bool_true(self):
        result = tfbool(true)
        self.assertIsInstance(result, TfBool)

    def test_bool_false(self):
        result = tfbool(false)
        self.assertIsInstance(result, TfBool)

    def test_true_str(self):
        result = str(tfbool(True))
        self.assertEqual(result, 'true')

    def test_false_str(self):
        result = str(tfbool(False))
        self.assertEqual(result, 'false')

    def test_get_type(self):
        result = tftype(tfbool(True))
        self.assertIs(result, TfBool)


class TestTfBoolLiteral(unittest.TestCase):

    def test_singleton_True(self):
        result = tfbool(True)
        self.assertIs(result, true)

    def test_singleton_False(self):
        result = tfbool(False)
        self.assertIs(result, false)

    def test_singleton_true(self):
        result = tfbool(true)
        self.assertIs(result, true)

    def test_singleton_false(self):
        result = tfbool(false)
        self.assertIs(result, false)

    def test_literal_True(self):
        result = tfbool(True)
        self.assertIsInstance(result, TfBoolLiteral)

    def test_literal_False(self):
        result = tfbool(False)
        self.assertIsInstance(result, TfBoolLiteral)

    def test_literal_true(self):
        result = tfbool(true)
        self.assertIsInstance(result, TfBoolLiteral)

    def test_literal_false(self):
        result = tfbool(false)
        self.assertIsInstance(result, TfBoolLiteral)
