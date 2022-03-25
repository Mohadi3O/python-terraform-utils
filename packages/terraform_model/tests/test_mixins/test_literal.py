# std
import types
import unittest

# internal
from terraform_model.all import *
from terraform_model.types.internal import *


class TestGetItem(unittest.TestCase):

    def test_literal_number_type(self):
        x = tfnumber(1)
        result = x.literal()
        self.assertIsInstance(result, int)

    def test_literal_number(self):
        x = tfnumber(1)
        result = x.literal()
        self.assertEqual(result, 1)
