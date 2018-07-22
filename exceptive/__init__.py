"""
Exceptive is a Python library that makes exception handling more programmatic and debuggable.
"""

__author__ = "Eray Erdin"
__copyright__ = "Copyright 2018, Eray Erdin"
__license__ = "Apache License 2.0"
__maintainer__ = "Eray Erdin"
__email__ = "eraygezer.94@gmail.com"
__status__ = "Prototype"
__version__ = "0.1.7"

class __Typing:
    Callable = callable
    Any = None


typing = __Typing

__all__ = ["inheritance.py", "decorators", "typing"]
