# std
import unittest

# internal
from terraform_model.all import *


class TestTfMatchKeys(unittest.TestCase):

    def test_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfString])
        z = variable('z', type=TfList[TfString])
        result = tfmatchkeys(x, y, z)
        self.assertIsInstance(result, TfList)

    def test_element_type(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfString])
        z = variable('z', type=TfList[TfString])
        result = tfmatchkeys(x, y, z).element_type()
        self.assertIs(result, TfString)

    def test_str(self):
        x = variable('x', type=TfList[TfString])
        y = variable('y', type=TfList[TfString])
        z = variable('z', type=TfList[TfString])
        result = str(tfmatchkeys(x, y, z))
        self.assertEqual(result, 'matchkeys(var.x, var.y, var.z)')
