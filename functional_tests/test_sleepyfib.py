from unittest import TestCase

import requests


class SleepyFibFunctionalTest(TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:8000/'

    def test_returns_fib_sequence(self):
        response = requests.get(self.base_url + 'fib/1')
        self.assertEqual(200, response.status_code)
        content = 'The largest number is: 0\nThe sequence is: [0]'
        self.assertEqual(content, response.content)

    def test_returns_400_for_string(self):
        response = requests.get(self.base_url + 'fib/boop')
        self.assertEqual(400, response.status_code)

    def test_returns_400_for_negative_number(self):
        response = requests.get(self.base_url + 'fib/-5')
        self.assertEqual(400, response.status_code)

    def test_returns_400_for_over_max_number(self):
        response = requests.get(self.base_url + 'fib/100000000000')
        self.assertEqual(400, response.status_code)

    def test_hello(self):
        response = requests.get(self.base_url + 'hello')
        self.assertEqual(200, response.status_code)
        content = 'Hello! Welcome to sleepyfib! \n'
        self.assertEqual(content, response.content)
