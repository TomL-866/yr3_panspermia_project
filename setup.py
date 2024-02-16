from setuptools import setup
from mypyc.build import mypycify

# List of modules to be compiled
modules = ["python/IMF/main.py", "python/IMF/functions.py", "python/helpers.py"]

setup(
    name="Project",
    ext_modules=mypycify(modules),
)
