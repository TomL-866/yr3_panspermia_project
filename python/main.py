"""Module contains main function to run program."""

import numpy as np

from python.functions import save_imf_values, plot_imf_histogram
from python.equations import quantile_func


def main() -> None:
    """Main function"""

    runs: int = 1_000_000

    u: np.ndarray = np.array([np.random.uniform(0, 1) for _ in range(runs)])
    stellar_mass_arr: np.ndarray = np.array(
        [quantile_func(u[x]) for x in range(runs)]
    )  # SI units

    save_imf_values(u, stellar_mass_arr)
    plot_imf_histogram(stellar_mass_arr)
