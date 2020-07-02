# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio-Records-Agent is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""High-level API for wokring with records, files, persistent identifers and search."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "pytest-invenio>=1.3.2",
]

invenio_search_version = '>=1.2.0,<2.0.0'

extras_require = {
    "docs": ["Sphinx>=3.0.0,<4.0.0",],
    # Elasticsearch version
    'elasticsearch6': [
        'invenio-search[elasticsearch6]{}'.format(invenio_search_version),
    ],
    'elasticsearch7': [
        'invenio-search[elasticsearch7]{}'.format(invenio_search_version),
    ],
    "tests": tests_require,
}

extras_require["all"] = []
for reqs in extras_require.values():
    extras_require["all"].extend(reqs)

install_requires = [
    "invenio-accounts>=1.3.0",
    "invenio-files-rest>=1.2.0",
    "invenio-pidstore>=1.2.0",
    "invenio-records-files>=1.2.1",
    "invenio-records-permissions>=0.8.0",
    "invenio-records>=1.3.2",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("invenio_records_agent", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="invenio-records-agent",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords="invenio records api",
    license="MIT",
    author="CERN",
    author_email="info@inveniosoftware.org",
    url="https://github.com/inveniosoftware/invenio-records-agent",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_base.apps": [
            "invenio_records_agent = invenio_records_agent:InvenioRecordsAgent",
        ],
        "invenio_base.api_apps": [
            "invenio_records_agent = invenio_records_agent:InvenioRecordsAgent",
        ],
        "invenio_config.module": [
            "invenio_records_agent = invenio_records_agent.config",
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 1 - Planning",
    ],
)
