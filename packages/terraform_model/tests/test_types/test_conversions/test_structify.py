# std
import unittest

# internal
from terraform_model.types.conversions.structify import structify, \
    TfNull, TfBool, TfNumber, TfString, TfList, TfMap, TfSet, TfObject


class TestStructify(unittest.TestCase):

    def test_null(self):
        result = structify('null')
        self.assertIs(result, TfNull)

    def test_bool(self):
        result = structify('bool')
        self.assertIs(result, TfBool)

    def test_number(self):
        result = structify('number')
        self.assertIs(result, TfNumber)

    def test_string(self):
        result = structify('string')
        self.assertIs(result, TfString)

    def test_list_string(self):
        result = structify(['list', 'string'])
        self.assertIs(result, TfList[TfString])

    def test_map_string(self):
        result = structify(['map', 'string'])
        self.assertIs(result, TfMap[TfString])

    def test_map_set(self):
        result = structify(['set', 'string'])
        self.assertIs(result, TfSet[TfString])

    def test_basic_object_no_name(self):
        definition = [
            "object",
            {
                "attribute_a": "string",
                "attribute_b": "string",
            }
        ]
        result = structify(definition)
        self.assertTrue(result.__name__.startswith('TfObject'))

    def test_basic_object_with_name(self):
        definition = [
            "object",
            {
                "attribute_a": "string",
                "attribute_b": "string",
            }
        ]
        result = structify(definition, 'basic_object')
        self.assertEqual(result.__name__, 'BasicObject')

    def test_basic_object_class_attributes(self):
        definition = [
            "object",
            {
                "attribute_a": "string",
                "attribute_b": "number",
            }
        ]
        result = structify(definition)
        with self.subTest('attribute class string'):
            self.assertIs(result.AttributeA, TfString)
        with self.subTest('attribute class number'):
            self.assertIs(result.AttributeB, TfNumber)
        with self.subTest('attribute property string'):
            self.assertIsInstance(result.attribute_a, property)
        with self.subTest('attribute property number'):
            self.assertIsInstance(result.attribute_b, property)

    def test_basic_object_instance_attributes(self):
        definition = [
            "object",
            {
                "attribute_a": "string",
                "attribute_b": "number",
            }
        ]
        result = structify(definition)
        instance = result(attribute_a='abc', attribute_b=123)
        with self.subTest('attribute property string'):
            self.assertEqual(instance.attribute_a.data, 'abc')
        with self.subTest('attribute property number'):
            self.assertEqual(instance.attribute_b.data, 123)

    def test_basic_object_instance_not_attribute(self):
        definition = [
            "object",
            {
                "attribute_a": "string",
                "attribute_b": "number",
            }
        ]
        result = structify(definition)
        instance = result(attribute_a='abc', attribute_b=123)
        with self.assertRaises(Exception):
            _ = instance.not_an_attribute

    def test_complex_object(self):
        definition = [
            "object",
            {
                "attribute_obj": [
                    "object",
                    {
                        "attribute_x": "number"
                    }
                ]
            }
        ]
        result = structify(definition)
        with self.subTest('attribute property object'):
            self.assertTrue(issubclass(result.AttributeObj, TfObject))
        with self.subTest('attribute property number'):
            self.assertIs(result.AttributeObj.AttributeX, TfNumber)
