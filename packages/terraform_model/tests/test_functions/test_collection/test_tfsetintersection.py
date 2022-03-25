# std
import unittest

# internal
from terraform_model.all import *


class TestTfSetIntersection(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfSet)
        result = tfsetintersection(x, y)
        self.assertIsInstance(result, TfSet)

    def test_element_type(self):
        x = variable('x', type=TfSet[TfString])
        y = variable('y', type=TfSet[TfString])
        result = tfsetintersection(x, y).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfSet)
        result = str(tfsetintersection(x, y))
        self.assertEqual(result, 'setintersection(var.x, var.y)')

    def test_many(self):
        x = variable('x', type=TfSet)
        y = variable('y', type=TfSet)
        z = variable('z', type=TfSet)
        result = str(tfsetintersection(x, y, z))
        self.assertEqual(result, 'setintersection(var.x, var.y, var.z)')
