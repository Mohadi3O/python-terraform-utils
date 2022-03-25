# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.collections.tflist import tflist, TfList, TfListLiteral
from terraform_model.utils.errors import TerraformTypeError


class TestTfList(unittest.TestCase):

    def test_tflist_list(self):
        result = tflist([1, 2])
        self.assertIsInstance(result, TfList)

    def test_tflist_list_str(self):
        result = str(tflist([1, 2]))
        self.assertEqual(result, '[\n  1,\n  2\n]')

    def test_non_similar_types(self):
        with self.assertRaises(TerraformTypeError):
            tflist([1, '2'])

    def test_element_type_number(self):
        x = variable('x', 1, type=TfNumber)
        l = tflist([x, 2])
        result = l.element_type()
        self.assertIs(result, TfNumber)

    def test_element_type_string(self):
        x = variable('x', 'abc', type=TfString)
        l = tflist([x, 'def'])
        result = l.element_type()
        self.assertIs(result, TfString)

    def test_chunk(self):
        l = variable('l', type=TfList[TfString])
        result = str(l.chunk(2))
        self.assertEqual('chunklist(var.l, 2)', result)

    def test_concat(self):
        a = variable('a', type=TfList[TfString])
        b = variable('b', type=TfList[TfString])
        result = str(a + b)
        self.assertEqual('concat(var.a, var.b)', result)

    def test_contains(self):
        l = variable('l', type=TfList[TfString])
        x = variable('x', type=TfString)
        result = str(l.contains(x))
        self.assertEqual('contains(var.l, var.x)', result)

    def test_distinct(self):
        l = variable('l', type=TfList[TfString])
        result = str(l.distinct())
        self.assertEqual('distinct(var.l)', result)

    def test_element(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        result = str(x.element(y))
        self.assertEqual(result, 'element(var.x, var.y)')

    def test_index(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfString)
        result = str(x.index(y))
        self.assertEqual(result, 'index(var.x, var.y)')

    def test_length(self):
        l = variable('l', type=TfList[TfString])
        result = str(l.length())
        self.assertEqual('length(var.l)', result)

    def test_reverse(self):
        l = variable('l', type=TfList[TfString])
        result = str(l.reverse())
        self.assertEqual('reverse(var.l)', result)

    def test_slice_both_indices(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfNumber)
        result = str(x.slice(y, z))
        self.assertEqual(result, 'slice(var.x, var.y, var.z)')

    def test_slice_start_index_only(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        result = str(x.slice(start=y))
        self.assertEqual(result, 'slice(var.x, var.y, length(var.x))')

    def test_slice_end_index_only(self):
        x = variable('x', type=TfList[TfString])
        z = variable('z', type=TfNumber)
        result = str(x.slice(end=z))
        self.assertEqual(result, 'slice(var.x, 0, var.z)')

    def test_sort(self):
        x = variable('x', type=TfList[TfString])
        result = str(x.sort())
        self.assertEqual(result, 'sort(var.x)')

    def test_getitem_element(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        result = str(x[y])
        self.assertEqual(result, 'var.x[var.y]')

    def test_getitem_slice_both_indices(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        z = variable('z', type=TfNumber)
        result = str(x[y:z])
        self.assertEqual(result, 'slice(var.x, var.y, var.z)')

    def test_getitem_slice_start_index_only(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfNumber)
        result = str(x[y:])
        self.assertEqual(result, 'slice(var.x, var.y, length(var.x))')

    def test_getitem_slice_end_index_only(self):
        x = variable('x', type=TfList[TfString])
        z = variable('z', type=TfNumber)
        result = str(x[:z])
        self.assertEqual(result, 'slice(var.x, 0, var.z)')


class TestTfListLiteral(unittest.TestCase):

    def test_literal_list(self):
        result = tflist([1, 2])
        self.assertIsInstance(result, TfListLiteral)
