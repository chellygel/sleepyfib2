SleepyFib 2.0
=============

SleepyFib is a REST API for producing the fibonacci sequence via API.

SleepyFib 2.0 uses Falcon. For more information about Falcon
you can visit their [documentation](http://falconframework.org/).

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

