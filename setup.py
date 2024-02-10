from setuptools import setup
from mypyc.build import mypycify

# List of modules to be compiled
modules = ["python/equations.py", "python/main.py", "python/functions.py"]

setup(
    name="Project",
    ext_modules=mypycify(modules),
)
