# coding: utf-8

"""
    kraken

    The core component of kraken-project

    The version of the OpenAPI document: 0.1.0
    Contact: git@omikron.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "kraken-sdk"
VERSION = "0.1.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "aiohttp >= 3.0.0",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="kraken",
    author="Niklas Pfister",
    author_email="git@omikron.dev",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "kraken"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="AGPL-3.0",
    long_description_content_type='text/markdown',
    long_description="""\
    The core component of kraken-project
    """,  # noqa: E501
    package_data={"kraken_sdk": ["py.typed"]},
)
