import numpy as np
from python.disk_calcs.calculate_density import find_radius, find_volume, find_density
from python.disk_calcs.plot_and_save import plot_disk_mass_vs_density


def main(stellar_mass_arr: np.ndarray) -> None:
    """Main function"""
    radius_arr: np.ndarray = np.vectorize(find_radius)(stellar_mass_arr)
    volume_arr: np.ndarray = np.vectorize(find_volume)(radius_arr)
    density_arr: np.ndarray = np.vectorize(find_density)(volume_arr, stellar_mass_arr)

    print("Plotting disk mass vs density...")
    plot_disk_mass_vs_density(stellar_mass_arr, density_arr)
