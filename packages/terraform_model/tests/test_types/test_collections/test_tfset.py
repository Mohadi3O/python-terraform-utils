# std
import unittest

# internal
from terraform_model.types.collections.tfset import TfSetLiteral
from terraform_model.all import *
from terraform_model.utils.errors import TerraformTypeError


class TestTfSet(unittest.TestCase):

    def test_tfset_set(self):
        result = tfset({1, 2})
        self.assertIsInstance(result, TfSet)

    def test_tfset_set_str(self):
        result = str(tfset({1, 2}))
        self.assertEqual(result, '[\n  1,\n  2\n]')

    def test_non_similar_types(self):
        with self.assertRaises(TerraformTypeError):
            tfset({1, '2'})

    def test_element_type_number(self):
        x = variable('x', 1, type=TfNumber)
        l = tfset({x, 2})
        result = l.element_type()
        self.assertIs(result, TfNumber)

    def test_element_type_string(self):
        x = variable('x', 'abc', type=TfString)
        l = tfset({x, 'def'})
        result = l.element_type()
        self.assertIs(result, TfString)

    def test_intersection(self):
        a = variable('a', type=TfSet)
        b = variable('b', type=TfSet)
        result = str(a & b)
        self.assertEqual('setintersection(var.a, var.b)', result)

    def test_subtract(self):
        a = variable('a', type=TfSet)
        b = variable('b', type=TfSet)
        result = str(a - b)
        self.assertEqual('setsubtract(var.a, var.b)', result)

    def test_union(self):
        a = variable('a', type=TfSet)
        b = variable('b', type=TfSet)
        result = str(a | b)
        self.assertEqual('setunion(var.a, var.b)', result)


class TestTfSetLiteral(unittest.TestCase):

    def test_literal_set(self):
        result = tfset({1, 2})
        self.assertIsInstance(result, TfSetLiteral)
