import numpy as np

from rust import get_stellar_masses
from python.IMF.plot_and_save import plot_imf_histogram

# from python.IMF.quantile_func import quantile_func  # Only uncomment if rust package is not working


def get_stellar_mass_array() -> np.ndarray:
    """Get stellar mass array from quantile function

    Returns:
        np.ndarray: Stellar mass array (SI units)
    """
    # # Uncomment this block if rust package is not working
    # runs: int = 1_000_000
    # print(f"Calling quantile function {runs:,} times...")
    # u: np.ndarray = np.random.uniform(0, 1, runs)
    # return np.vectorize(quantile_func)(u)
    print("Calculating stellar masses...")
    return np.array(get_stellar_masses(), dtype=float)


def main(stellar_mass_arr: np.ndarray) -> None:
    """Main function"""
    print("Plotting IMF histogram...")
    plot_imf_histogram(stellar_mass_arr)
