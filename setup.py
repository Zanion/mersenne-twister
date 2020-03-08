from setuptools import find_packages
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_type = Extension(
    "mt_random_type",
    sources=["**/*.pyx", "src/lib/mt19937ar-struct.c"],
    include_dirs=["src/lib"]
)

setup(
    name="mersenne_random",
    packages=find_packages(where='src', exclude=['test']),
    ext_modules = cythonize([ext_type])
)
