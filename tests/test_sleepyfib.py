import unittest

import falcon
from itertools import islice

from sleepyfib.sleepyfib import FibonacciResource, MAX_FIB


class TestValidateSleepyFib(unittest.TestCase):

    def test_validate_fib_negative_number(self):
        fib_res = FibonacciResource()
        self.assertRaises(falcon.HTTPInvalidParam, fib_res.validate_fib, -1)

    def test_validate_fib_exceed_maximum_number(self):
        fib_res = FibonacciResource()
        num = MAX_FIB + 1
        self.assertRaises(falcon.HTTPInvalidParam, fib_res.validate_fib, num)

    def test_validate_fib_str(self):
        fib_res = FibonacciResource()
        self.assertRaises(falcon.HTTPInvalidParam, fib_res.validate_fib, 'boo')

    def test_validate(self):
        fib_res = FibonacciResource()
        fib_num = fib_res.validate_fib(5)
        self.assertEquals(5, fib_num)
