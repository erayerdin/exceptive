Annotation Module
=================

The Approach
------------

Annotation-based approach is a good choice;

 - if you do not want to use inheritance on your classes
 - if you want to implement ``exceptive`` on a simpler case, like a simple method

Annotations are much more flexible than inheritance, in which you can define custom object method to run and custom
object method to run on exception.

catch
-----

``catch`` is an annotation which you can apply on an independent method as below::

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

You can also proive positional or keyword arguments for callback method on annotation. Here is a code sample::

    def invalid_input(exception, default_value):
        print("The input is invalid.")

    @catch(TypeError, invalid_input, default_value="world")
    def greet(name):
        print("Hello "+name+"!")

    greet("Eray")
    # Hello Eray!

    greet(5)
    # Hello world!

