Inheritance Module
==================

The Approach
------------
Inheritance-based approach is a good choice;

 - if you want to isolate your functionality in one class
 - if you want to standardize the exception-handling

MethodicExceptive
-----------------

``MethodicExceptive`` is a class with ``__call__`` method. All you have to do is to provide a ``run`` method and
``except__YourException`` on it.

You can import ``MethodicExceptive`` from ``exceptive.inheritance`` module and inherit it on your class.::

    class Hello(MethodicExceptive):
        def run(self, name):
            print("Hello "+name+"!")

        def except__TypeError(self, exception):
            print("Invalid input!")

        # Initialize your object.
        obj = Hello()

        # Call it.
        obj("world")
        # Hello world!

        obj(5)
        # Invalid input!

You can also provide ``except__else`` to handle exception that are not provided as method.::

    class Hello(MethodicExceptive):
        def run(self, name):
            print("Hello world!")

        def except__TypeError(self, exception):
            pass  # do something with TypeError

        def except__else(self, exception):
            pass  # do something with any other exception
