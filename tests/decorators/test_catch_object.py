import unittest

from exceptive.decorators import catch_object


class Class1:
    @catch_object(TypeError)
    def hello_world(self, name: str):
        return "Hello "+name+"!"

    def except__TypeError(self, e: TypeError):
        return False


class Class2:
    @catch_object(TypeError, "handle_type_error")
    def hello_world(self, name: str):
        return "Hello "+name+"!"

    def handle_type_error(self, e: TypeError):
        return False


class Class3:
    @catch_object(TypeError)
    @catch_object(AttributeError)
    def hello_world(self, name: str, attr: str, *args):  # attr here will be strip for test case
        name = getattr(name, attr)(*args)
        return "Hello " + name + "!"

    def except__TypeError(self, e: TypeError):
        return 0

    def except__AttributeError(self, e: AttributeError):
        return 1


class Class4:
    @catch_object(TypeError, "handle_type_error")
    @catch_object(AttributeError, "handle_attribute_error")
    def hello_world(self, name: str, attr: str, *args):  # attr here will be strip for test case
        name = getattr(name, attr)(*args)
        return "Hello " + name + "!"

    def handle_type_error(self, e: TypeError):
        return 0

    def handle_attribute_error(self, e: AttributeError):
        return 1


class TestCatchObjectDecorator(unittest.TestCase):
    def test_one_standard(self):
        obj = Class1()
        val = obj.hello_world("world")
        self.assertEqual(val, "Hello world!")

        val = obj.hello_world(5)
        self.assertFalse(val)

    def test_one_custom(self):
        obj = Class2()
        val = obj.hello_world("world")
        self.assertEqual(val, "Hello world!")

        val = obj.hello_world(5)
        self.assertFalse(val)

    def test_multiple_standard(self):
        obj = Class3()

        val = obj.hello_world("world", "strip")
        self.assertEqual(val, "Hello world!")

        val = obj.hello_world(5, "__add__", 1)
        self.assertEqual(val, 0)  # TypeError

        val = obj.hello_world("world", "attribute_that_does_not_exist")
        self.assertEqual(val, 1)  # AttributeError

    def test_multiple_custom(self):
        obj = Class4()

        val = obj.hello_world("world", "strip")
        self.assertEqual(val, "Hello world!")

        val = obj.hello_world(5, "__add__", 1)
        self.assertEqual(val, 0)  # TypeError

        val = obj.hello_world("world", "attribute_that_does_not_exist")
        self.assertEqual(val, 1)  # AttributeError
