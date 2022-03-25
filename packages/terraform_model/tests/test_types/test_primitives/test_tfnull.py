# std
import unittest

# internal
from terraform_model.types.primitives.tfnull import tfnull, TfNull, TfNullLiteral, null
from terraform_model.internal.tftype import tftype


class TestTfNull(unittest.TestCase):

    def test_tfnull_opt(self):
        result = tfnull()
        self.assertIsInstance(result, TfNull)

    def test_tfnull_None(self):
        result = tfnull(None)
        self.assertIsInstance(result, TfNull)

    def test_tfnull_null(self):
        result = tfnull(null)
        self.assertIsInstance(result, TfNull)

    def test_tfnull_str(self):
        result = str(tfnull())
        self.assertEqual(result, 'null')

    def test_get_type(self):
        result = tftype(tfnull())
        self.assertIs(result, TfNull)


class TestTfNullLiteral(unittest.TestCase):

    def test_singleton_opt(self):
        result = tfnull()
        self.assertIs(result, null)

    def test_singleton_None(self):
        result = tfnull(None)
        self.assertIs(result, null)

    def test_singleton_null(self):
        result = tfnull(null)
        self.assertIs(result, null)

    def test_literal(self):
        result = tfnull()
        self.assertIsInstance(result, TfNullLiteral)
