import unittest

from exceptive import exceptives


##############
# Exceptives #
##############
class Exceptive1(exceptives.MethodicExceptive):
    def run(self, name):
        return "Hello "+name


class Exceptive2(Exceptive1):
    def except_TypeError(self, exception: TypeError):
        return False


class Exceptive3(exceptives.MethodicExceptive):
    def run(self, attribute: str):
        return getattr("Whatever", attribute)


class Exceptive4(Exceptive3):
    def except_AttributeError(self, exception: AttributeError):
        return None

#########
# Tests #
#########
class TestMethodicExceptive(unittest.TestCase):
    def test_normal(self):
        exc = Exceptive1()

        try:
            hello = exc("Eray")
            self.assertEqual(hello, "Hello Eray")
        except Exception as e:
            self.fail(str(e))

    def test_overriding_except_TypeError(self):
        exc = Exceptive2()

        hello = exc(5) # a fairly random number
        self.assertFalse(hello)

    def test_except_AttributeError(self):
        exc = Exceptive3()

        with self.assertRaises(AttributeError):
            attr = exc("attribute_that_does_not_exist")

    def test_overriding_except_AttributeError(self):
        exc = Exceptive4()

        try:
            attr = exc("attribute_that_does_not_exist_again")
        except Exception as e:
            self.fail(str(e))
