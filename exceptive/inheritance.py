"""
This module contains all exceptive types.
"""
try:
    import typing
except ImportError:
    class Typing:
        Any = None
    typing = Typing


class BaseExceptive:
    def run(self, *args, **kwargs) -> typing.Any:
        """
        This is a function that will run on __call__ method.

        :param args:
        :param kwargs:
        :return:
        """
        pass

    def except__else(self, exception: BaseException) -> typing.Any:
        """
        This function runs if the exception is not registered.

        :param exception:
        :return:
        """
        raise exception


class MethodicExceptive(BaseExceptive):
    def __call__(self, *args, **kwargs) -> typing.Any:
        try:
            return self.run(*args, **kwargs)
        except BaseException as e1:
            try:
                exception_method_string = "except__{}".format(e1.__class__.__name__)
                func = getattr(self, exception_method_string)
                return func(e1)
            except AttributeError:
                return self.except__else(e1)
