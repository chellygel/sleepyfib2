SleepyFib 2.0
=============

SleepyFib is a REST API for producing the fibonacci sequence via API.

SleepyFib 2.0 uses Falcon. For more information about Falcon
you can visit their [documentation](http://falconframework.org/).

SleepyFib2 supports a maximum value of 10000. This is in the interest of
performance. This API will only accept positive, whole integers only!

This guide assumes the user has little experience with python. If you have
some suggestions, questions, or concerns please don't hesitate to contact me!

##Setting Up

Before getting started, please ensure that you have installed the necessary
requirements. Requirements will be maintained within the [requirements.txt]
(https://github.com/chelseawinfree/sleepyfib2/blob/master/requirements.txt)
file.

To install these requirements perform the following:
<pre>
pip install -r requirements.txt
</pre>

For the purpose of this tutorial we will assume that you wish to run this
service locally. We recommend you use gunicorn to launch the application.
We have provided [dev-requirements.txt]
(https://github.com/chelseawinfree/sleepyfib2/blob/master/dev-requirements.txt)
for you to install instead.

Please visit [Gunicorn's page](http://gunicorn.org/) for more information.

##Launching the application using Gunicorn

To launch the application, you simply type this command:
<pre>
gunicorn sleepyfib:app
</pre>

This will launch the application in terminal for you.

##Making a Call to SleepyFib

Current supported calls to SleepyFib are as follows:

Fibonacci Sequence:
<pre>
curl localhost:8000/fib/5

>The largest number is: 3
>The sequence is: [0, 1, 1, 2, 3]
</pre>

Fibonacci Hello:
<pre>
curl localhost:8000/hello

>Hello! Welcome to sleepyfib!
</pre>

##Testing

In order to run the tests you must have the test requirements installed!

To kick the tests off, use py.test or tox.

<pre>
tox -e py27

===================================================================== test session starts =====================================================================
platform darwin -- Python 2.7.6 -- py-1.4.30 -- pytest-2.7.2
collected 5 items

tests/test_fibonacci.py .
tests/test_sleepyfib.py ....

================================================================== 5 passed in 0.05 seconds ===================================================================
py27 runtests: commands[1] | coverage combine
py27 runtests: commands[2] | coverage report -m
Name                  Stmts   Miss Branch BrMiss  Cover   Missing
-----------------------------------------------------------------
sleepyfib/__init__        0      0      0      0   100%
sleepyfib/fibonacci       6      0      2      1    88%
sleepyfib/sleepyfib      32      9      6      2    71%   11-12, 34-42
-----------------------------------------------------------------
TOTAL                    38      9      8      3    74%
___________________________________________________________________________ summary ___________________________________________________________________________
  py27: commands succeeded
  congratulations :)
</pre>
