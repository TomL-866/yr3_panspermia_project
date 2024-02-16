"""Module contains main function to run program."""

import numpy as np

from python.IMF.plot_and_save import plot_imf_histogram
from python.IMF.quantile_func import quantile_func


def main() -> None:
    """Main function"""

    runs: int = 10_000_000
    print(f"Running {runs:,} iterations of quantile function...")
    u: np.ndarray = np.random.uniform(0, 1, runs)
    stellar_mass_arr: np.ndarray = np.vectorize(quantile_func)(u)  # SI units

    print("Plotting IMF histogram...")
    plot_imf_histogram(stellar_mass_arr)
