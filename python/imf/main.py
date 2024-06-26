import numpy as np

from rust import get_stellar_masses
from imf.plot_and_save import plot_imf_histogram, save_imf_values
from helpers import load_stellar_mass_file


def get_stellar_mass_array() -> np.ndarray:
    """Returns the array of stellar masses.
    This function uses values from the Rust library.
    To see the source code, look in the `rust/src` directory.

    Returns:
        np.ndarray: Stellar mass array (SI)
    """
    print("Calculating stellar masses...")
    return np.array(get_stellar_masses(), dtype=float)
    # return load_stellar_mass_file()


def main(stellar_mass: np.ndarray) -> None:
    print("Plotting IMF histogram...")
    plot_imf_histogram(stellar_mass)

    print("Saving stellar mass array...")
    save_imf_values(stellar_mass)
