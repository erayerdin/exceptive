# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.1.8] - 2018-07-22
### Fixed
 - Wrong referencer in `__all__` variable in `exceptive/__init__.py`
 - Call to `except__else` rather than `except_else` on `MethodicExceptive`

## [0.1.7] - 2018-07-22
### Added
 - documentation

### Changed
 - `exceptives` module to `inheritance` module
 - `except_WhateverError` to Django-style `except__WhateverError`

### Removed
 - the documentation on readme

## [0.1.3] - 2018-07-21
### Added
 - `decorators` package and its utilities
 - `catch` decorator for method
 - `catch_object` decorator for object method

## [0.1.1] - 2018-07-21
### Added
 - TravisCI support
 - Coveralls support

### Changed
 - Long description content type

## [0.1.0a0] - 2018-07-20
### Added
 - `BaseExceptive` for custom exceptive construction
 - `MethodicExceptive` for object-method-based exceptives
