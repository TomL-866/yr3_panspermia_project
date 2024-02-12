"""Module contains main function to run program."""

import numpy as np

from python.functions import plot_imf_histogram, save_imf_values
from python.equations import quantile_func


def main() -> None:
    """Main function"""

    runs: int = 1_000_000

    u = np.random.uniform(0, 1, runs)
    stellar_mass_arr = np.vectorize(quantile_func)(u)  # SI units

    print("Saving IMF values to CSV...")
    save_imf_values(u, stellar_mass_arr)
    print("Plotting IMF histogram...")
    plot_imf_histogram(stellar_mass_arr)
