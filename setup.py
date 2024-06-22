# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def readme():
    with open("README.md", encoding="utf-8") as readme_file:
        return readme_file.read()


# Extract version. Cannot import directly because of import error.
root_dir = os.path.dirname(__file__)
with open(os.path.join(root_dir, "condo/__init__.py"), "r") as f:
    for line in f.readlines():
        if line.startswith("__version__"):
            version = line.split("=")[-1].strip().strip('"')
            break


install_reqs = [
    "numpy",
    "pytorch-minimize>=0.0.2",
    "scipy",
    "scikit-learn",
    "torch>=1.4.0",
]
configuration = {
    "name": "condo",
    "version": version,
    "description": "Confounded domain adaptation",
    "long_description": readme(),
    "long_description_content_type": "text/markdown",
    "classifiers": [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    "keywords": "domain adaptation",
    "packages": ["condo"],
    "install_requires": install_reqs,
    "python_requires": ">=3.8",
    "ext_modules": [],
    "cmdclass": {},
    "test_suite": "nose.collector",
    "tests_require": ["nose"],
    "data_files": (),
    "zip_safe": True,
}

setup(**configuration)
