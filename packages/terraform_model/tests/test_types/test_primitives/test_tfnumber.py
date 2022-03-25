# std
import unittest

# internal
from terraform_model.types.primitives.tfnumber import tfnumber, TfNumber, TfNumberLiteral
from terraform_model.internal.tftype import tftype


class TestTfNumber(unittest.TestCase):

    def test_tfnumber_int(self):
        result = tfnumber(1)
        self.assertIsInstance(result, TfNumber)

    def test_tfnumber_float(self):
        result = tfnumber(1.0)
        self.assertIsInstance(result, TfNumber)

    def test_tfnumber_int_str(self):
        result = str(tfnumber(1))
        self.assertEqual(result, '1')

    def test_tfnumber_float_str(self):
        result = str(tfnumber(1.0))
        self.assertEqual(result, '1.0')

    def test_get_type(self):
        result = tftype(tfnumber(1))
        self.assertIs(result, TfNumber)


class TestTfNumberLiteral(unittest.TestCase):

    def test_literal_int(self):
        result = tfnumber(1)
        self.assertIsInstance(result, TfNumberLiteral)

    def test_literal_float(self):
        result = tfnumber(1.0)
        self.assertIsInstance(result, TfNumberLiteral)
