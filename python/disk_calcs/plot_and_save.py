import matplotlib.pyplot as plt
import astropy.constants as astro_const
import numpy as np
from python.helpers import get_base_dir


def plot_disk_mass_vs_density(disk_mass: np.ndarray, disk_density: np.ndarray) -> None:
    disk_mass = np.sort(disk_mass)
    disk_density = np.sort(disk_density)

    plt.plot(disk_mass / astro_const.M_sun.value, disk_density)
    plt.xlabel("Disk Mass ($M_\\odot$)")
    plt.ylabel("Disk Density (kg/m$^3$)")
    plt.savefig(f"{get_base_dir()}/output/graphs/disk_mass_vs_density.png")
    plt.close()
