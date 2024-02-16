from setuptools import setup
from mypyc.build import mypycify

# List of modules to be compiled
modules = [
    "python/IMF/main.py",
    "python/IMF/plot_and_save.py",
    "python/helpers.py",
    "python/disk_calcs/main.py",
    "python/disk_calcs/plot_and_save.py",
]

setup(
    name="Project",
    ext_modules=mypycify(modules),
)
