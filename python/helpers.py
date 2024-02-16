import os

def get_base_dir() -> str:
    """This function returns the base directory of the project"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))