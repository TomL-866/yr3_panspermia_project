"""Module contains main function to run program."""

import numpy as np

from python.functions import plot_imf_histogram
from python.equations import quantile_func


def main() -> None:
    """Main function"""

    runs: int = 1_000_000

    u: np.ndarray = np.random.uniform(0, 1, runs)
    stellar_mass_arr: np.ndarray = np.vectorize(quantile_func)(u)  # SI units

    print("Plotting IMF histogram...")
    plot_imf_histogram(stellar_mass_arr)
