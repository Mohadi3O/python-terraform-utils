# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTypify(unittest.TestCase):

    def test_typify_True(self):
        result = typify(True)
        self.assertIs(result, true)

    def test_typify_true(self):
        result = typify(true)
        self.assertIs(result, true)

    def test_typify_False(self):
        result = typify(False)
        self.assertIs(result, false)

    def test_typify_false(self):
        result = typify(false)
        self.assertIs(result, false)

    def test_typify_None(self):
        result = typify(None)
        self.assertIs(result, null)

    def test_typify_null(self):
        result = typify(null)
        self.assertIs(result, null)

    def test_typify_int(self):
        result = typify(1)
        self.assertIsInstance(result, TfNumberLiteral)

    def test_typify_float(self):
        result = typify(1.0)
        self.assertIsInstance(result, TfNumberLiteral)

    def test_typify_str(self):
        result = typify('abc')
        self.assertIsInstance(result, TfStringLiteral)

    def test_typify_tflist_empty(self):
        result = typify([])
        self.assertIsInstance(result, TfList)

    def test_typify_tflist(self):
        result = typify([1])
        self.assertIsInstance(result, TfList)

    def test_typify_tflist_multiple_types(self):
        with self.assertRaises(TerraformTypeError):
            _ = typify([1, 'a'])

    def test_typify_tfmap_empty(self):
        result = typify({})
        self.assertIsInstance(result, TfMap)

    def test_typify_tfmap(self):
        result = typify({'x': 1})
        self.assertIsInstance(result, TfMap)

    def test_typify_tfmap_multiple_types(self):
        with self.assertRaises(TerraformTypeError):
            _ = typify({'x': 1, 'y': 'b'})

    def test_typify_tfset_empty(self):
        result = typify(set())
        self.assertIsInstance(result, TfSet)

    def test_typify_tfset(self):
        result = typify({1, })
        self.assertIsInstance(result, TfSet)

    def test_typify_tfset_multiple_types(self):
        with self.assertRaises(TerraformTypeError):
            _ = typify({1, 'a'})
