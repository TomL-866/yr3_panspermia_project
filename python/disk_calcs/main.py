import numpy as np
from python.disk_calcs.calculate_density import (
    find_disk_radius,
    find_volume,
    find_density,
    find_dust_mass,
)
from python.disk_calcs.plot_and_save import plot_dust_mass_vs_disk_density


def main(stellar_mass_arr: np.ndarray) -> None:
    """Main function"""
    radius_arr: np.ndarray = np.vectorize(find_disk_radius)(stellar_mass_arr)
    volume_arr: np.ndarray = np.vectorize(find_volume)(radius_arr)
    density_arr: np.ndarray = np.vectorize(find_density)(volume_arr, stellar_mass_arr)

    print("Plotting dust mass vs disk density...")
    plot_dust_mass_vs_disk_density(find_dust_mass(stellar_mass_arr), density_arr)
