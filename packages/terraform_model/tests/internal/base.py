# std
import unittest


class BaseTestClass(unittest.TestCase):

    def assertPossibleGenericsEqual(self, expected, result):
        if hasattr(expected, '__origin__') and hasattr(result, '__origin__'):
            fail_msg = f'{expected} != {result}'
            if expected.__origin__ != result.__origin__:
                self.fail(fail_msg)
            if len(expected.__args__) != len(result.__args__):
                self.fail(fail_msg)
            for expected_arg, result_arg in zip(expected.__args__, result.__args__):
                self.assertPossibleGenericsEqual(expected_arg, result_arg)
        else:
            self.assertEqual(expected, result)
