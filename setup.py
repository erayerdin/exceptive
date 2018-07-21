try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as f:
    LONG_DESC = f.read()

setup(
    name="exceptive",
    version="0.1.3",
    description="Exceptive is a Python library that makes exception handling more programmatic and debuggable.",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    author="Eray Erdin",
    author_email="eraygezer.94@gmail.com",
    url="https://github.com/erayerdin/exceptive",
    download_url="https://github.com/erayerdin/exceptive/archive/master.zip",
    license="Apache License 2.0",
    packages=["exceptive"],
    include_package_data=True,
    tests_require=["nose", "coverage", "tox"],
    zip_safe=False,
    test_suite="tests.runtests",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Software Development :: Testing"
    ]
)
