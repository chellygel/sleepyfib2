

class SleepyFib:
    """Basic Functions and Validators for SleepyFib """

    def calc_fib(self, n):
        # Fibonacci sequence generator
        a, b = 0, 1
        for _ in xrange(n):
            yield a
            a, b = b, a + b
