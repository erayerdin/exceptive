Basics
======

Installation
------------

You can either use ``pip`` to install the package::

    pip install exceptive
    # you can use pip3 explicitly if you also have Python 2 in your development environment

Or simply download the package, extract it and use ``setup.py``::

    python3 setup.py build
    python3 setup.py install

Simple Usage
------------

You can use ``catch`` decorator to simply define the callback method to run in case of a particular exception occurs::

    def typeerror_fallback_function(exception):
        print("Invalid input.")

    @catch(TypeError, typeerror_fallback_function)
    def greet(name):
        print("Hello "+name+"!")

    greet("world")
    # Hello world!

    greet(5)  # int value raises TypeError when concatenated with str directly
    # Invalid input.

