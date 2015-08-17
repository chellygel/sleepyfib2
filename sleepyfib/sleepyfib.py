import falcon

from fibonacci import SleepyFib


MAX_FIB = 10000


class HelloResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Hello! Welcome to sleepyfib! \n'


class FibonacciResource:

    def on_get(self, req, resp, fib_num):
        sleepy_fib = SleepyFib()

        try:
            fib_num = int(fib_num)
        except:
            raise falcon.HTTPInvalidParam('Positive Integers Only!', fib_num)

        if fib_num > MAX_FIB:
            msg = ('{} exceeds the maximum of {}'.format(fib_num, MAX_FIB))
            raise falcon.HTTPInvalidParam(msg, fib_num)

        if fib_num <= 0:
            raise falcon.HTTPInvalidParam('Positive Integers Only!', fib_num)

        fib_list = []
        for i in sleepy_fib.calc_fib(fib_num):
            fib_list.append(i)
        resp.body = ('The largest number is: {}\n'
                     'The sequence is: {}'.format(fib_list[-1], fib_list))
        resp.status = falcon.HTTP_200


app = falcon.API()

hello = HelloResource()
fib = FibonacciResource()

app.add_route('/hello', hello)
app.add_route('/fib/{fib_num}', fib)
