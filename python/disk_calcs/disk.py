import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astro_const
from helpers import get_base_dir


class DiskCalcs:
    """This class is here to group together functions that calculate
    values for the disk around the star."""

    def __init__(self, stellar_mass: np.ndarray):
        self.stellar_mass: np.ndarray = stellar_mass
        self.radius: np.ndarray = np.vectorize(self.find_radius)(
            stellar_mass
        )  # Disk radius
        self.reduced_radius: np.ndarray = np.vectorize(self.reduce_radius)(
            self.radius
        )  # Reduced disk radius
        self.volume: np.ndarray = np.vectorize(self.find_volume_slab_geometry)(
            self.reduced_radius
        )  # Disk volume
        self.density: np.ndarray = np.vectorize(self.find_density)(
            self.volume, stellar_mass
        )  # Disk density

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

        plt.figure()
        plt.plot(disk_density * 1000 / 100**3, dust_mass / astro_const.M_sun.value)
        plt.ylabel("Dust Mass (M$_\\odot$)")
        plt.xlabel("Disk Density (g/cm$^3$)")
        plt.title("Dust Mass vs Disk Density for Slab Volume Geometry")
        plt.savefig(f"{get_base_dir()}/output/graphs/dust_mass_vs_disk_density.png")
        plt.close()

    def run(self) -> None:
        self.plot_dust_mass_vs_disk_density(
            self.find_dust_mass(self.stellar_mass), self.density
        )
