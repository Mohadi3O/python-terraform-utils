# std
from types import GenericAlias
from typing import Union
import unittest

# internal
from tests.internal.base import BaseTestClass
from terraform_model.all import *
from terraform_model.types.internal import *
from terraform_model.internal.tftype import tftype, is_instance


class TestTfType(unittest.TestCase):

    def test_tfnull(self):
        result = tftype(null)
        self.assertEqual(TfNull, result)

    def test_tfnull_literal(self):
        result = tftype(None)
        self.assertEqual(TfNull, result)

    def test_tfnull_type(self):
        result = tftype(type(None))
        self.assertEqual(TfNull, result)

    def test_tfnull_tftype(self):
        result = tftype(TfNull)
        self.assertEqual(TfNull, result)

    def test_tfnull_tftype_literal(self):
        result = tftype(TfNullLiteral)
        self.assertEqual(TfNull, result)

    def test_tfnull_local(self):
        result = tftype(local('x', None))
        self.assertEqual(TfNull, result)

    def test_tfnull_variable_default(self):
        result = tftype(variable('x', null))
        self.assertEqual(TfNull, result)

    def test_tfnull_variable_type(self):
        result = tftype(variable('x', type=TfNull))
        self.assertEqual(TfNull, result)

    def test_tfbool(self):
        result = tftype(true)
        self.assertEqual(TfBool, result)

    def test_tfbool_literal(self):
        result = tftype(True)
        self.assertEqual(TfBool, result)

    def test_tfbool_type(self):
        result = tftype(bool)
        self.assertEqual(TfBool, result)

    def test_tfbool_tftype(self):
        result = tftype(TfBool)
        self.assertEqual(TfBool, result)

    def test_tfbool_tftype_literal(self):
        result = tftype(TfBoolLiteral)
        self.assertEqual(TfBool, result)

    def test_tfbool_local(self):
        result = tftype(local('x', True))
        self.assertEqual(TfBool, result)

    def test_tfbool_variable_default(self):
        result = tftype(variable('x', True))
        self.assertEqual(TfBool, result)

    def test_tfbool_variable_type(self):
        result = tftype(variable('x', type=TfBool))
        self.assertEqual(TfBool, result)

    def test_tfnumber(self):
        result = tftype(tfnumber(1))
        self.assertEqual(TfNumber, result)

    def test_tfnumber_literal(self):
        result = tftype(1)
        self.assertEqual(TfNumber, result)

    def test_tfnumber_type_int(self):
        result = tftype(int)
        self.assertEqual(TfNumber, result)

    def test_tfnumber_type_float(self):
        result = tftype(float)
        self.assertEqual(TfNumber, result)

    def test_tfnumber_tftype(self):
        result = tftype(TfNumber)
        self.assertEqual(TfNumber, result)

    def test_tfnumber_tftype_literal(self):
        result = tftype(TfNumberLiteral)
        self.assertEqual(TfNumber, result)

    def test_tfnumber_local(self):
        result = tftype(local('x', 1))
        self.assertEqual(TfNumber, result)

    def test_tfnumber_variable_default(self):
        result = tftype(variable('x', 1))
        self.assertEqual(TfNumber, result)

    def test_tfnumber_variable_type(self):
        result = tftype(variable('x', type=TfNumber))
        self.assertEqual(TfNumber, result)

    def test_tfstring(self):
        result = tftype(tfstring('abc'))
        self.assertEqual(TfString, result)

    def test_tfstring_literal(self):
        result = tftype('abc')
        self.assertEqual(TfString, result)

    def test_tfstring_type(self):
        result = tftype(str)
        self.assertEqual(TfString, result)

    def test_tfstring_tftype(self):
        result = tftype(TfString)
        self.assertEqual(TfString, result)

    def test_tfstring_tftype_literal(self):
        result = tftype(TfStringLiteral)
        self.assertEqual(TfString, result)

    def test_tfstring_local(self):
        result = tftype(local('x', 'abc'))
        self.assertEqual(TfString, result)

    def test_tfstring_variable_default(self):
        result = tftype(variable('x', 'abc'))
        self.assertEqual(TfString, result)

    def test_tfstring_variable_type(self):
        result = tftype(variable('x', type=TfString))
        self.assertEqual(TfString, result)

    def test_tflist(self):
        result = tftype(tflist([]))
        self.assertEqual(TfList, result)

    def test_tflist_literal(self):
        result = tftype([])
        self.assertEqual(TfList, result)

    def test_tflist_type(self):
        result = tftype(list)
        self.assertEqual(TfList, result)

    def test_tflist_tftype(self):
        result = tftype(TfList)
        self.assertEqual(TfList, result)

    def test_tflist_tftype_literal(self):
        result = tftype(TfListLiteral)
        self.assertEqual(TfList, result)

    def test_tflist_local(self):
        result = tftype(local('x', []))
        self.assertEqual(TfList, result)

    def test_tflist_variable_default(self):
        result = tftype(variable('x', []))
        self.assertEqual(TfList, result)

    def test_tflist_variable_type(self):
        result = tftype(variable('x', type=TfList))
        self.assertEqual(TfList, result)

    def test_tfset(self):
        result = tftype(tfset(set()))
        self.assertEqual(TfSet, result)

    def test_tfset_literal(self):
        result = tftype(set())
        self.assertEqual(TfSet, result)

    def test_tfset_type(self):
        result = tftype(set)
        self.assertEqual(TfSet, result)

    def test_tfset_tftype(self):
        result = tftype(TfSet)
        self.assertEqual(TfSet, result)

    def test_tfset_tftype_literal(self):
        result = tftype(TfSetLiteral)
        self.assertEqual(TfSet, result)

    def test_tfset_local(self):
        result = tftype(local('x', set()))
        self.assertEqual(TfSet, result)

    def test_tfset_variable_default(self):
        result = tftype(variable('x', set()))
        self.assertEqual(TfSet, result)

    def test_tfset_variable_type(self):
        result = tftype(variable('x', type=TfSet))
        self.assertEqual(TfSet, result)

    def test_tfmap(self):
        result = tftype(tfmap(dict()))
        self.assertEqual(TfMap, result)

    def test_tfmap_literal(self):
        result = tftype(dict())
        self.assertEqual(TfMap, result)

    def test_tfmap_type(self):
        result = tftype(dict)
        self.assertEqual(TfMap, result)

    def test_tfmap_tftype(self):
        result = tftype(TfMap)
        self.assertEqual(TfMap, result)

    def test_tfmap_tftype_literal(self):
        result = tftype(TfMapLiteral)
        self.assertEqual(TfMap, result)

    def test_tfmap_local(self):
        result = tftype(local('x', dict()))
        self.assertEqual(TfMap, result)

    def test_tfmap_variable_default(self):
        result = tftype(variable('x', dict()))
        self.assertEqual(TfMap, result)

    def test_tfmap_variable_type(self):
        result = tftype(variable('x', type=TfMap))
        self.assertEqual(TfMap, result)

    def test_generic_shallow(self):
        generic = GenericAlias(TfList, (TfUnknown,))
        result = tftype(generic)
        expected = TfList
        self.assertEqual(expected, result)

    def test_tflist_shallow(self):
        result = tftype(tflist(['abc']))
        expected = TfList
        self.assertEqual(expected, result)


class TestTfTypeDeep(BaseTestClass):

    def test_tflist_literal_empty(self):
        result = tftype([], deep=True)
        expected = GenericAlias(TfList, (TfUnknown,))
        self.assertPossibleGenericsEqual(expected, result)

    def test_tflist_literal(self):
        result = tftype(['abc'], deep=True)
        expected = GenericAlias(TfList, (TfString,))
        self.assertPossibleGenericsEqual(expected, result)

    def test_tflist_empty(self):
        result = tftype(tflist([]), deep=True)
        expected = GenericAlias(TfList, (TfUnknown,))
        self.assertPossibleGenericsEqual(expected, result)

    def test_tflist_type(self):
        result = tftype(list, deep=True)
        self.assertEqual(TfList, result)

    def test_tflist_tftype_deep(self):
        result = tftype(TfList, deep=True)
        self.assertEqual(TfList, result)

    def test_tflist_local(self):
        result = tftype(local('x', []), deep=True)
        expected = GenericAlias(TfList, (TfUnknown,))
        self.assertEqual(expected, result)

    def test_tflist_variable_default(self):
        result = tftype(variable('x', []), deep=True)
        expected = GenericAlias(TfList, (TfUnknown,))
        self.assertEqual(expected, result)

    def test_tflist_variable_type(self):
        result = tftype(variable('x', type=TfList), deep=True)
        self.assertEqual(TfList, result)

    def test_tflist_type_deep(self):
        result = tftype(['abc'], deep=True)
        expected = GenericAlias(TfList, (TfString,))
        self.assertPossibleGenericsEqual(expected, result)

    def test_tfset_type_deep(self):
        result = tftype({'abc'}, deep=True)
        expected = GenericAlias(TfSet, (TfString,))
        self.assertPossibleGenericsEqual(expected, result)

    def test_tfmap_type_deep(self):
        result = tftype({'x': 1}, deep=True)
        expected = GenericAlias(TfMap, (TfNumber,))
        self.assertPossibleGenericsEqual(expected, result)

    def test_deep_tfmap_type(self):
        v = variable('x', type=TfMap[TfList[TfString]])
        result = tftype(v)
        expected = TfMap
        self.assertEqual(expected, result)

    def test_deep_tfmap_type_deep(self):
        v = variable('x', type=TfMap[TfList[TfString]])
        result = tftype(v, deep=True)
        expected = GenericAlias(TfMap, (TfList[TfString],))
        self.assertPossibleGenericsEqual(expected, result)

    def test_deep_tfmap_literal_type_deep(self):
        l = local('x', {'x': ['abc']})
        result = tftype(l, deep=True)
        expected = GenericAlias(TfMap, (TfList[TfString],))
        self.assertPossibleGenericsEqual(expected, result)

    def test_tflist_deep(self):
        result = tftype(tflist(['abc']), deep=True)
        expected = GenericAlias(TfList, (TfString,))
        self.assertPossibleGenericsEqual(expected, result)


class TestIsInstance(BaseTestClass):

    def test_python_type(self):
        self.assertTrue(is_instance(1, int))

    def test_terraform_type(self):
        self.assertTrue(is_instance(tfnumber(1), TfNumber))

    def test_with_tuple_types(self):
        self.assertTrue(is_instance(tfnumber(1), (TfNumber, TfString)))

    def test_types(self):
        self.assertTrue(is_instance(TfNumber, TfNumber))

    def test_generics(self):
        self.assertTrue(is_instance(TfList[TfString], TfList[TfString]))

    def test_generic_and_generic_alias(self):
        self.assertTrue(is_instance(TfList[TfString], GenericAlias(TfList, (TfString,))))

    def test_union(self):
        self.assertTrue(is_instance(TfNumber, Union[TfNumber, TfString]))

    def test_generic_full(self):
        self.assertTrue(is_instance(tflist(['abc']), TfList[TfString]))

    def test_generic_shallow(self):
        self.assertTrue(is_instance(tfmap({'x': [1]}), TfMap[TfList]))
