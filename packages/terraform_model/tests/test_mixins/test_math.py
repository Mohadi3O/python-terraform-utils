# std
import types
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import *


class TestGetItem(unittest.TestCase):

    def test_add(self):
        result = tfnumber(1) + tfnumber(2)
        self.assertIsInstance(result, TfNumber)

    def test_add_str(self):
        result = str(tfnumber(1) + tfnumber(2))
        self.assertEqual(result, '(1 + 2)')

    def test_sub(self):
        result = tfnumber(1) - tfnumber(2)
        self.assertIsInstance(result, TfNumber)

    def test_sub_str(self):
        result = str(tfnumber(1) - tfnumber(2))
        self.assertEqual(result, '(1 - 2)')

    def test_mul(self):
        result = tfnumber(1) * tfnumber(2)
        self.assertIsInstance(result, TfNumber)

    def test_mul_str(self):
        result = str(tfnumber(1) * tfnumber(2))
        self.assertEqual(result, '(1 * 2)')

    def test_div(self):
        result = tfnumber(1) / tfnumber(2)
        self.assertIsInstance(result, TfNumber)

    def test_div_str(self):
        result = str(tfnumber(1) / tfnumber(2))
        self.assertEqual(result, '(1 / 2)')

    def test_mod(self):
        result = tfnumber(1) % tfnumber(2)
        self.assertIsInstance(result, TfNumber)

    def test_mod_str(self):
        result = str(tfnumber(1) % tfnumber(2))
        self.assertEqual(result, '(1 % 2)')
