import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astro_const
from helpers import get_base_dir


class DiskCalcs:
    """This class is here to group together functions that calculate
    values for the disk around a star.

    It takes in a stellar mass and calculates the radius, reduced radius,
    volume, mass, dust mass, and density of the disk.

    Run the run() method to plot dust mass vs disk density."""

    def __init__(self, stellar_mass: np.ndarray):
        print("Calculating disk values...")
        self.stellar_mass: np.ndarray = stellar_mass
        self.disk_mass: np.ndarray = self.find_mass(stellar_mass)  # Disk mass
        self.radius: np.ndarray = self.find_radius(stellar_mass)  # Disk radius
        self.reduced_radius: np.ndarray = self.reduce_radius(
            self.radius
        )  # Reduced disk radius
        self.volume: np.ndarray = self.find_volume_slab_geometry(
            self.reduced_radius
        )  # Disk volume
        self.density: np.ndarray = self.find_density(
            self.volume, stellar_mass
        )  # Disk density
        self.csa_sideview = self.find_csa_sideview(
            self.reduced_radius
        )  # Cross sectional area of disk from side view
        self.csa_topview = self.find_csa_topview(
            self.reduced_radius
        )  # Cross sectional area of disk from top view

    def get_radius(self) -> np.ndarray:
        return self.radius

    def get_reduced_radius(self) -> np.ndarray:
        return self.reduced_radius

    def get_mass(self) -> np.ndarray:
        return self.disk_mass

    def get_csa_sideview(self) -> np.ndarray:
        return self.csa_sideview

    def get_csa_topview(self) -> np.ndarray:
        return self.csa_topview

    def find_radius(self, stellar_mass: np.ndarray) -> np.ndarray:
        # This function is based on Equation 13
        # from https://doi.org/10.1093/mnras/stac1513

        au_to_m: float = astro_const.au.value
        m_sun: float = astro_const.M_sun.value
        return 200 * au_to_m * (stellar_mass / m_sun) ** (0.3)

    def reduce_radius(self, disk_radius: np.ndarray) -> np.ndarray:
        # TODO: This is known rubbish. We'll come back to it later
        return disk_radius / 1

    def find_volume_slab_geometry(self, disk_radius: np.ndarray) -> np.ndarray:
        au_to_m: float = astro_const.au.value
        disk_height: float = 0.1 * 1 * au_to_m
        circumference: float = 2 * np.pi * disk_radius
        return disk_radius * disk_height * circumference

    def find_csa_sideview(self, disk_radius: np.ndarray) -> np.ndarray:
        au_to_m: float = astro_const.au.value
        disk_height: float = 0.1 * au_to_m
        return disk_radius * disk_height

    def find_csa_topview(self, disk_radius: np.ndarray) -> np.ndarray:
        return np.pi * disk_radius**2

    def find_mass(self, stellar_mass: np.ndarray) -> np.ndarray:
        return 0.1 * stellar_mass

    def find_dust_mass(self, stellar_mass: np.ndarray) -> np.ndarray:
        return 0.01 * self.find_mass(stellar_mass)

    def find_density(
        self, disk_volume: np.ndarray, stellar_mass: np.ndarray
    ) -> np.ndarray:
        dust_mass = self.find_dust_mass(stellar_mass)
        return (
            dust_mass / disk_volume
        )  # Expecting this to be 1 g/cm^3. If not, need to reduce the radius a lot more. Assume dust tightly packed in the central plane of disk

    def plot_dust_mass_vs_disk_density(
        self, dust_mass: np.ndarray, disk_density: np.ndarray
    ) -> None:
        print("Plotting dust mass vs disk density...")
        dust_mass = np.sort(dust_mass)  # SI units
        disk_density = np.sort(disk_density)  # SI units

        plt.figure()
        plt.plot(disk_density * 1000 / 100**3, dust_mass / astro_const.M_sun.value)
        plt.ylabel("Dust Mass (M$_\\odot$)")
        plt.xlabel("Disk Density (g/cm$^3$)")
        plt.title("Dust Mass vs Disk Density for Slab Volume Geometry")
        plt.savefig(f"{get_base_dir()}/output/graphs/dust_mass_vs_disk_density.png")
        # plt.savefig(f"{get_base_dir()}/output/graphs/dust_mass_vs_disk_density.pgf")
        plt.close()

    def save_disk_density(self, disk_density: np.ndarray) -> None:
        print("Saving disk density values...")
        np.save(
            f"{get_base_dir()}/output/values/disk_density.npy",
            disk_density,
        )

    def run(self) -> None:
        self.plot_dust_mass_vs_disk_density(
            self.find_dust_mass(self.stellar_mass), self.density
        )

        self.save_disk_density(self.density)
