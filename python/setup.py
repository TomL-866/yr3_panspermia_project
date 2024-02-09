from setuptools import setup, find_packages
from mypyc.build import mypycify

# Find all .py files in the current directory
import glob

py_files = glob.glob("./*.py")

setup(
    name="mypyc_compiled_project",
    packages=find_packages(),
    ext_modules=mypycify(py_files),
)
