import numpy as np
import os
from math import floor, log10


def get_base_dir() -> str:
    """Returns the base directory of the project.
    This is the directory that contains the `python` directory.

    Returns:
        str: The base directory of the project.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_stellar_mass_file() -> np.ndarray:
    """This function returns the array of stellar masses
    by loading the .npy file from the output/values directory.

    Returns:
        np.ndarray: Stellar masses array (SI)
    """
    base_dir: str = get_base_dir()
    stellar_mass: str = np.load(f"{base_dir}/output/values/stellar_masses.npy")
    return stellar_mass


def sig_figs(x: float, precision: int) -> float:
    """Rounds a number to given number of significant figures.
    Code taken from https://mattgosden.medium.com/rounding-to-significant-figures-in-python-2415661b94c3

    Args:
        x (float): Number to round
        precision (int): Number of significant figures

    Returns:
        float: Rounded number
    """

    x = float(x)
    precision = int(precision)

    return round(x, -int(floor(log10(abs(x)))) + (precision - 1))
