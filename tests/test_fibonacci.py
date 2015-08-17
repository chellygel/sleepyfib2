import unittest

from itertools import islice

from sleepyfib.fibonacci import SleepyFib


class TestFib(unittest.TestCase):

    def test_calc_fib(self):
        sleepy_fib = SleepyFib()
        fib_gen = sleepy_fib.calc_fib(5)
        fib_tup = (0, 1, 1, 2, 3)
        self.assertEqual(tuple(islice(fib_gen, 5)), fib_tup)
