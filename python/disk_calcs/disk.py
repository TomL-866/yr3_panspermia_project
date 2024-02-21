import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astro_const
from helpers import get_base_dir


class Disk:
    def __init__(self):
        pass

    def find_radius(self, stellar_mass: float) -> float:
        """Get disk radius from stellar mass.
        This function is based on Equation 13
        from https://doi.org/10.1093/mnras/stac1513

        Args:
            stellar_mass (float): Stellar mass in SI units
        Returns:
            float: Radius of disk in SI units
        """
        au_to_m: float = 1.49597871e11
        m_sun: float = 1.98840987e30  # SI units
        return 200 * au_to_m * (stellar_mass / m_sun) ** (0.3)

    def reduce_radius(self, disk_radius: float) -> float:
        return disk_radius / 10

    def find_volume(self, disk_radius: float) -> float:
        """Get disk volume from disk radius and height

        Args:
            disk_radius (float): Radius of disk in SI units
        Returns:
            float: Volume of disk in SI units
        """
        au_to_m: float = 1.49597871e11
        disk_height: float = 0.1 * 1 * au_to_m
        return np.pi * disk_radius**2 * disk_height

    def find_volume_slab_geometry(self, disk_radius: float) -> float:
        """Get disk volume from disk radius and height using slab geometry

        Args:
            disk_radius (float): Radius of disk in SI units
        Returns:
            float: Volume of disk in SI units
        """
        au_to_m: float = 1.49597871e11
        disk_height: float = 0.1 * 1 * au_to_m
        return disk_radius * disk_height

    def find_mass(self, stellar_mass: float) -> float:
        """Get disk mass from stellar mass

        Args:
            stellar_mass (float): Stellar mass in SI units
        Returns:
            float: Mass of disk in SI units
        """
        return 0.1 * stellar_mass

    def find_dust_mass(self, stellar_mass: float) -> float:
        """Get dust mass from stellar mass

        Args:
            stellar_mass (float): Stellar mass in SI units
        Returns:
            float: Mass of dust in disk in SI units
        """
        return 0.01 * self.find_mass(stellar_mass)

    def find_density(self, disk_volume: float, stellar_mass: float) -> float:
        """Get disk density from disk volume and stellar mass

        Args:
            disk_volume (float): Volume of disk in SI units
            stellar_mass (float): Stellar mass in SI units
        Returns:
            float: Density of disk in SI units
        """
        dust_mass = self.find_dust_mass(stellar_mass)
        return dust_mass / disk_volume

    def plot_dust_mass_vs_disk_density(
        self, dust_mass: np.ndarray, disk_density: np.ndarray
    ) -> None:
        dust_mass = np.sort(dust_mass)  # SI units
        disk_density = np.sort(disk_density)  # SI units

        plt.plot(disk_density * 1000 / 100**3, dust_mass / astro_const.M_sun.value)
        plt.ylabel("Dust Mass (M$_\\odot$)")
        plt.xlabel("Disk Density (g/cm$^3$)")
        plt.savefig(f"{get_base_dir()}/output/graphs/dust_mass_vs_disk_density.png")
        plt.close()

    def find_dust_radius(self, disk_radius: float) -> float:
        return 0.1 * disk_radius

    def run(self, stellar_mass_arr: np.ndarray) -> None:
        # All values in the following arrays are in SI units and
        # are for the disk around the star
        radius_arr: np.ndarray = np.vectorize(self.find_radius)(
            stellar_mass_arr
        )  # Disk radius

        reduced_radius_arr: np.ndarray = np.vectorize(self.reduce_radius)(radius_arr)

        volume_arr: np.ndarray = np.vectorize(self.find_volume_slab_geometry)(
            reduced_radius_arr
        )  # Disk volume

        density_arr: np.ndarray = np.vectorize(self.find_density)(
            volume_arr, stellar_mass_arr
        )  # Disk density

        self.plot_dust_mass_vs_disk_density(
            self.find_dust_mass(stellar_mass_arr), density_arr
        )
