"""Module contains functions useful for completing parts of the project"""

from typing import Sequence
import os
import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astro_const


def get_base_dir() -> str:
    """This function returns the base directory of the project"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def plot_imf_histogram(stellar_mass_array: np.ndarray) -> None:
    """This function plots a histogram of the stellar mass array
    and saves in the output/graphs directory.

    Args:
        stellar_mass_array (np.ndarray): Stellar mass array (SI units) from quantile func (see equations.py)
    """

    plt.figure()
    bins: list[float] = list(np.logspace(0, np.log10(50), num=50))
    plt.hist(
        stellar_mass_array / astro_const.M_sun.value,
        bins=bins,
    )
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("Stellar Mass (M$_{Sun}$)")
    plt.ylabel("Frequency")
    plt.savefig(get_base_dir() + "/output/graphs/imf_histogram.png")


def save_imf_values(u: np.ndarray, stellar_mass_array: np.ndarray) -> None:
    """This function saves u and stellar mass values to a CSV file

    Args:
        u (np.ndarray): Array of random numbers between 0 and 1
        stellar_mass_array (np.ndarray): Stellar mass array (SI units) from quantile func (see equations.py)
    """

    csv_dir = get_base_dir() + "/output/csv"
    np.savetxt(
        csv_dir + "/imf_values.csv",
        np.column_stack((u, stellar_mass_array)),
        delimiter=",",
        header="u,stellar_mass",
        comments="",
    )
