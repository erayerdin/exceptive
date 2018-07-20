# Exceptive

[![PyPI - Version](https://img.shields.io/pypi/v/exceptive.svg)](https://pypi.org/project/exceptive/)
[![PyPI - License](https://img.shields.io/pypi/l/exceptive.svg)](LICENSE.txt)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/exceptive.svg)](https://pypi.org/project/exceptive/)
[![PyPI - Status](https://img.shields.io/pypi/status/exceptive.svg)](https://pypi.org/project/exceptive/)
[![Travis](https://img.shields.io/travis/erayerdin/exceptive.svg)](http://travis-ci.org/erayerdin/exceptive)
[![Coveralls github](https://img.shields.io/coveralls/github/erayerdin/exceptive.svg)](https://coveralls.io/github/erayerdin/exceptive)

Exceptive is a Python library that makes exception handling more programmatic
and debuggable.

## Usage
First, import `exceptives` packages for any exceptive class as such:

    from exceptive import exceptives

### Exception Handling with Object Methods

You can provide custom methods for exceptions:

    class HelloWorld(exceptives.MethodicExceptive):
        def run(self, name):
            print("Hello "+name+"!")
        
        def except_TypeError(self, exception):
            print("Invalid value!")
            # or you can use a logger here
    
    func = HelloWorld()
    func("world")
    # Hello world!
    
    func(5)
    # Invalid value!

`run` function is the core of your object. When you call your object like
a function, whatever inside the `run` function will be executed.

In case you didn't register your exception as a method named
`except_YourException`, you can provide an `except_else` method to get
the exception instance and do what you want to do with it. Example;

    class HelloWorld(exceptives.MethodicExceptive):
        def run(self, name):
            print("Hello "+name+"!")
        
        def except_else(self, exception):
            print("Something unexpected happened!")
            
        func = HelloWorld()
        func("world")
        # Hello world!
        
        func(5)
        # Something unexpected happened!

Since the `HelloWorld` class above does not have any `except_TypeError`
method, the `TypeError` instance exception will be passed to `except_else`
method.
