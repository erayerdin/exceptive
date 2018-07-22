Decorator Module
=================

The Approach
------------
Decorator-based approach is a good choice;

 - if you do not want to use inheritance on your classes
 - if you want to implement ``exceptive`` on a simpler case, like a simple method

Decorators are much more flexible than inheritance, in which you can define custom object method to run and custom
object method to run on exception.

catch
-----
.. py:function:: catch(exception, method[, *args[, **kwargs]])

You can import the ``catch`` decorator from ``exceptive.decorators`` module.

``catch`` is a decorator which you can apply on an independent method as below::

    def invalid_input(exception):
        print("The input is invalid.")

    @catch(TypeError, invalid_input)
    def greet(name):
        print("Hello "+name+"!")

    greet("world")
    # Hello world!

    greet(5)
    # The input is invalid.

First you provide which exception to catch and then a callback method, which might be a proper method or a lambda.

Notice you have ``exception`` on callback method? That's how you can further analysis the thrown exception and provide
further custom behavior.

You can also proive positional or keyword arguments for callback method on decorator. Here is a code sample::

    def invalid_input(exception, default_value):
        print("Hello "+default_value+"!")

    @catch(TypeError, invalid_input, default_value="world")
    def greet(name):
        print("Hello "+name+"!")

    greet("Eray")
    # Hello Eray!

    greet(5)
    # Hello world!

.. warning::
    This decorator is not suitable for object methods. For object methods, see ``catch_object`` decorator below.

.. note::
    You can also use multiple ``catch`` decorator to handle multiple exception types.

catch_object
------------
.. py:function:: catch(exception, [method=None[, *args[, **kwargs]]])

``catch_object`` decorator is specifically designed for *object methods*. It looks up for callback method in the
object-level.

You can import ``catch_object`` decorator from ``exceptive.decorators``.

Providing Default Callback Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When you provide ``catch_object`` decorator with ``YourException``, ``except__YourException`` is called in case the
exception is thrown.::

    class Hello:
        @catch_object(TypeError)
        def greet(self, name):
            print("Hello "+name+"!")

        def except__TypeError(self, exception):
            print("Invalid value!")

Providing Custom Callback Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Default lookup for callback method may generate stylistic warnings by your intellisense or linters. So, you can also
provide the method name to look up for as a ``str`` to handle exception.::

    class Hello:
        @catch_object(TypeError, "handle_type_error")
        def greet(self, name):
            print("Hello "+name+"!")

        def handle_type_error(self, exception):
            print("Invalid value!")

``method`` argument also accepts ``callable``s, so that you can pass an independent method.::

    def handle_type_error(exception):
        print("Invalid value!")

    class Hello:
        @catch_object(TypeError, handle_type_error)
        def greet(self, name):
            print("Hello "+name+"!")

.. note::
    ``catch_object`` decorator's parameters are quite similar to ``catch`` decorator's. So you can also provide your
    own ``args`` and ``kwargs`` to it.

.. note::
    You can also define multiple ``catch_object`` on a single object method.
