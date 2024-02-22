import numpy as np

from rust import get_stellar_masses
from IMF.plot_and_save import plot_imf_histogram, save_imf_values


def get_stellar_mass_array() -> np.ndarray:
    """Get stellar mass array from quantile function

    Returns:
        np.ndarray: Stellar mass array (SI units)
    """
    print("Calculating stellar masses...")
    return np.array(get_stellar_masses(), dtype=float)


def main(stellar_mass: np.ndarray) -> None:
    """Main function"""
    print("Plotting IMF histogram...")
    plot_imf_histogram(stellar_mass)

    print("Saving stellar mass array...")
    save_imf_values(stellar_mass)
