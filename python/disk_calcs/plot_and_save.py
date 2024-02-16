import matplotlib.pyplot as plt
import astropy.constants as astro_const
import numpy as np
from python.helpers import get_base_dir


def plot_dust_mass_vs_disk_density(
    dust_mass: np.ndarray, disk_density: np.ndarray
) -> None:
    dust_mass = np.sort(dust_mass)
    disk_density = np.sort(disk_density)

    plt.plot(disk_density, dust_mass / astro_const.M_sun.value)
    plt.ylabel("Dust Mass ($M_\\odot$)")
    plt.xlabel("Disk Density (kg/m$^3$)")
    plt.savefig(f"{get_base_dir()}/output/graphs/dust_mass_vs_disk_density.png")
    plt.close()
