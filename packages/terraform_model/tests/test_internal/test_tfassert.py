# std
from types import GenericAlias
import unittest

# internal
from terraform_model.all import *
from terraform_model.internal import tfassert
from terraform_model.utils.errors import TerraformTypeError


class TestIsInstance(unittest.TestCase):

    def test_tfnull(self):
        tfassert.is_instance(null, TfNull)

    def test_not_tfnull(self):
        with self.assertRaises(TerraformTypeError):
            tfassert.is_instance(1, TfNull)


class TestSameType(unittest.TestCase):

    def test_same_type_primitive(self):
        x = tfnumber(1)
        y = tfnumber(2)
        tfassert.same_type(x, y)

    def test_not_same_type_primitive(self):
        x = tfnumber(1)
        y = tfstring('2')
        with self.assertRaises(TerraformTypeError):
            tfassert.same_type(x, y)

    def test_same_type_collection(self):
        x = tflist([1])
        y = tflist([2])
        tfassert.same_type(x, y)

    def test_same_type_collection_element_type_mismatch(self):
        x = tflist([1])
        y = tflist(['a'])
        tfassert.same_type(x, y)

    def test_not_same_type_collection(self):
        x = tflist([1])
        y = tfset({2, })
        with self.assertRaises(TerraformTypeError):
            tfassert.same_type(x, y)


class TestSameTypeDeep(unittest.TestCase):

    def test_same_type_primitive(self):
        x = tfnumber(1)
        y = tfnumber(2)
        tfassert.same_type_deep(x, y)

    def test_not_same_type_primitive(self):
        x = tfnumber(1)
        y = tfstring('2')
        with self.assertRaises(TerraformTypeError):
            tfassert.same_type_deep(x, y)

    def test_same_type_collection(self):
        x = tflist([1])
        y = tflist([2])
        tfassert.same_type_deep(x, y)

    def test_same_type_collection_element_type_mismatch(self):
        x = tflist([1])
        y = tflist(['a'])
        with self.assertRaises(TerraformTypeError):
            tfassert.same_type_deep(x, y)

    def test_not_same_type_collection(self):
        x = tflist([1])
        y = tfset({2, })
        with self.assertRaises(TerraformTypeError):
            tfassert.same_type_deep(x, y)


class TestSameElementType(unittest.TestCase):

    def test_same_primitive(self):
        x = tflist([1])
        y = tflist([2])
        tfassert.same_element_type(x, y)

    def test_not_same_primitive(self):
        x = tflist([1])
        y = tflist(['a'])
        with self.assertRaises(TerraformTypeError):
            tfassert.same_element_type(x, y)

    def test_same_collection(self):
        x = tflist([tflist([1])])
        y = tflist([tflist([2])])
        tfassert.same_element_type(x, y)

    def test_same_collection_deep_mismatch(self):
        x = tflist([tflist([1])])
        y = tflist([tflist(['a'])])
        tfassert.same_element_type(x, y)

    def test_not_same_collection(self):
        x = tflist([tflist([1])])
        y = tflist([tfset({2, })])
        with self.assertRaises(TerraformTypeError):
            tfassert.same_element_type(x, y)


class TestSameElementTypeDeep(unittest.TestCase):

    def test_same_primitive(self):
        x = tflist([1])
        y = tflist([2])
        tfassert.same_element_type_deep(x, y)

    def test_not_same_primitive(self):
        x = tflist([1])
        y = tflist(['a'])
        with self.assertRaises(TerraformTypeError):
            tfassert.same_element_type_deep(x, y)

    def test_same_collection(self):
        x = tflist([tflist([1])])
        y = tflist([tflist([2])])
        tfassert.same_element_type_deep(x, y)

    def test_same_collection_deep_mismatch(self):
        x = tflist([tflist([1])])
        y = tflist([tflist(['a'])])
        with self.assertRaises(TerraformTypeError):
            tfassert.same_element_type_deep(x, y)

    def test_not_same_collection(self):
        x = tflist([tflist([1])])
        y = tflist([tfset({2, })])
        with self.assertRaises(TerraformTypeError):
            tfassert.same_element_type_deep(x, y)
