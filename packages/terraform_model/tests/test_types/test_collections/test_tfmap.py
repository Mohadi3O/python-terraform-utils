# std
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.collections.tfmap import tfmap, TfMap, TfMapLiteral
from terraform_model.utils.errors import TerraformTypeError


class TestTfMap(unittest.TestCase):

    def test_tfmap_list(self):
        result = tfmap({'x': 1, 'y': 2})
        self.assertIsInstance(result, TfMap)

    def test_tfmap_list_str(self):
        result = str(tfmap({'x': 1, 'y': 2}))
        self.assertEqual(result, '{\n  "x": 1,\n  "y": 2\n}')

    def test_non_similar_types(self):
        with self.assertRaises(TerraformTypeError):
            tfmap({'x': 1, 'y': 'abc'})

    def test_element_type_number(self):
        x = variable('x', 1, type=TfNumber)
        m = tfmap({'x': x, 'y': 2})
        result = m.element_type()
        self.assertIs(result, TfNumber)

    def test_element_type_string(self):
        x = variable('x', 'abc', type=TfString)
        m = tfmap({'x': x, 'y': 'def'})
        result = m.element_type()
        self.assertIs(result, TfString)

    def test_tfkeys_type(self):
        x = variable('x', type=TfMap)
        result = x.keys()
        self.assertIsInstance(result, TfList)

    def test_tfkeys_element_type(self):
        x = variable('x', type=TfMap)
        result = x.keys().element_type()
        self.assertIs(result, TfString)

    def test_tfkeys_str(self):
        x = variable('x', type=TfMap)
        result = str(x.keys())
        self.assertEqual(result, 'keys(var.x)')

    def test_tfvalues_str(self):
        x = variable('x', type=TfMap)
        result = str(x.values())
        self.assertEqual(result, 'values(var.x)')

    def test_length_type(self):
        result = tfmap({}).length()
        self.assertIsInstance(result, TfNumber)

    def test_lookup_type(self):
        x = variable('x', type=TfMap[TfNumber])
        result = x.lookup('y', 2)
        self.assertIsInstance(result, TfNumber)

    def test_lookup_str(self):
        x = variable('x', type=TfMap[TfNumber])
        result = str(x.lookup('y', 2))
        self.assertEqual(result, 'lookup(var.x, "y", 2)')

    def test_getitem_str(self):
        x = variable('x', type=TfMap[TfNumber])
        result = str(x['y'])
        self.assertEqual(result, 'var.x["y"]')

    def test_merge_type(self):
        x = variable('x', type=TfMap[TfNumber])
        y = variable('y', type=TfMap[TfNumber])
        result = x.merge(y)
        self.assertIsInstance(result, TfMap)

    def test_merge_element_type(self):
        x = variable('x', type=TfMap[TfNumber])
        y = variable('y', type=TfMap[TfNumber])
        result = x.merge(y).element_type()
        self.assertIs(result, TfNumber)

    def test_merge_str(self):
        x = variable('x', type=TfMap[TfNumber])
        y = variable('y', type=TfMap[TfNumber])
        result = str(x.merge(y))
        self.assertEqual(result, 'merge(var.x, var.y)')

    def test_merge_dunder_add(self):
        x = variable('x', type=TfMap[TfNumber])
        y = variable('y', type=TfMap[TfNumber])
        result = str(x + y)
        self.assertEqual(result, 'merge(var.x, var.y)')


class TestTfMapLiteral(unittest.TestCase):

    def test_literal_list(self):
        result = tfmap({'x': 1, 'y': 2})
        self.assertIsInstance(result, TfMapLiteral)
