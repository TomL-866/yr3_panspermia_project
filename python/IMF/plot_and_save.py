import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astro_const

from helpers import get_base_dir


def plot_imf_histogram(stellar_mass_array: np.ndarray) -> None:
    """This function plots a histogram of the stellar mass array
    and saves in the output/graphs directory.

    Args:
        stellar_mass_array (np.ndarray): Stellar mass array (SI units) from quantile func (see equations.py)
    """

    plt.figure()
    bins: list[float] = list(np.logspace(np.log10(0.01), np.log10(50), num=75))
    plt.hist(
        stellar_mass_array / astro_const.M_sun.value,
        bins=bins,
    )
    plt.xlim(10**-2, 10**2)
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("Stellar Mass (M$_{\\odot}$)")
    plt.ylabel("Frequency")
    plt.title("Initial Mass Function (IMF) Histogram")
    plt.savefig(get_base_dir() + "/output/graphs/imf_histogram.png")
    plt.close()


def save_imf_values(stellar_mass_array: np.ndarray) -> None:
    """This function saves u and stellar mass values to a .npy file

    Args:
        u (np.ndarray): Array of random numbers between 0 and 1
        stellar_mass_array (np.ndarray): Stellar mass array (SI units) from quantile func (see equations.py)
    """

    values_dir: str = get_base_dir() + "/output/values"
    np.save(values_dir + "/stellar_masses", stellar_mass_array)
