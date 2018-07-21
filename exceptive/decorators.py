try:
    import typing
except ImportError:
    from exceptive import typing
from functools import wraps


class __Catch:
    """
    A decorator for catching exceptions on a method and applying custom methods in case the exception is thrown.
    """
    def __init__(self, exception: BaseException, method: typing.Callable, *args, **kwargs):
        """
        :param exception: Exception to catch.
        :param method: Method to apply.
        :param args: Positional arguments for method to apply.
        :param kwargs: Keyword arguments for method to apply.
        """
        self.__exception = exception
        self.__method = method
        self.__params = (args, kwargs)

    def __call__(self, func: typing.Callable, *args, **kwargs) -> typing.Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self.__exception as e:
                return self.__method(e, *self.__params[0], **self.__params[1])
        return wrapper


class __CatchObject:
    """
    A decorator for catching exceptions on an object method and applying custom methods in case the exception is thrown.
    """
    def __init__(self, exception: BaseException, method=None, *args, **kwargs):
        """
        :param exception: Exception to catch.
        :param method: Method to apply. If it is str, the method is searched inside the object attributes. If it is
        callable, it is executed.
        :param args: Positional arguments for method to apply.
        :param kwargs: Keyword arguments for method to apply.
        """
        self.__exception = exception

        if method:
            self.__method = method  # type: callable
        else:
            self.__method = "except__{}".format(exception.__name__)

        self.__params = (args, kwargs)

    def __call__(self, func: typing.Callable, *args, **kwargs):
        @wraps(func)
        def wrapper(obj: object, *args, **kwargs):
            try:
                return func(obj, *args, **kwargs)
            except self.__exception as e:
                if isinstance(self.__method, str):
                    try:
                        f = getattr(obj, self.__method)
                    except AttributeError:
                        if hasattr(obj, "except__else"):
                            f = getattr(obj, "except__else")
                        else:
                            raise e
                    return f(e)
                else:
                    return self.__method(e)

        return wrapper


catch = __Catch
catch_object = __CatchObject
__all__ = ["catch", "catch_object"]
