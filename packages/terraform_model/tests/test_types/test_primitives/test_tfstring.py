# std
import unittest

# internal
from terraform_model.all import TfNumber, tfstring, TfString, TfStringLiteral
from terraform_model.internal.tftype import tftype


class TestTfString(unittest.TestCase):

    def test_tfstring(self):
        result = tfstring('abc')
        self.assertIsInstance(result, TfString)

    def test_tfstring_str(self):
        result = str(tfstring('abc'))
        self.assertEqual(result, '"abc"')

    def test_get_type(self):
        result = tftype(tfstring('abc'))
        self.assertIs(result, TfString)

    def test_length_type(self):
        result = tfstring('').length()
        self.assertIsInstance(result, TfNumber)


class TestTfStringLiteral(unittest.TestCase):

    def test_literal(self):
        result = tfstring('abc')
        self.assertIsInstance(result, TfStringLiteral)
