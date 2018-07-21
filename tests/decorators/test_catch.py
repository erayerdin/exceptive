import unittest

from exceptive.decorators import catch


@catch(TypeError, lambda e: None)
def method1(name):
    return "Hello "+name+"!"


@catch(TypeError, lambda e, word: "Hello "+word+"!", word="world")
def method2(name):
    return "Hello "+name+"!"


@catch(TypeError, lambda e: 0)
@catch(AttributeError, lambda e: 1)
def method3(name, attr):  # attr here will be strip for test case
    name = getattr(name, attr)()
    return "Hello "+name+"!"


class TestCatchDecorator(unittest.TestCase):
    def test_typeerror_noargs(self):
        val = method1("world")
        self.assertEqual(val, "Hello world!")

        val = method1(5)
        self.assertIsNone(val)

    def test_typeerror_kwargs(self):
        val = method2("Eray")
        self.assertEqual(val, "Hello Eray!")

        val = method2(5)
        self.assertEqual(val, "Hello world!")

    def test_multiple_args_noargs(self):
        val = method3("world", "strip")
        self.assertEqual(val, "Hello world!")

        val = method3(5, "__add__", 1)  # TypeError
        self.assertEqual(val, 0)

        val = method3("world", "an_attr_that_does_not_exist")  # AttributeError
        self.assertEqual(val, 1)
