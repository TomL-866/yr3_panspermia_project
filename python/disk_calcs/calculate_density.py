import numpy as np
from numba import njit


@njit
def find_disk_radius(stellar_mass: float) -> float:
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


@njit
def find_volume(disk_radius: float) -> float:
    """Get volume from disk radius and height

    Args:
        disk_radius (float): Radius of disk in SI units
    Returns:
        float: Volume of disk in SI units
    """
    au_to_m: float = 1.49597871e11
    disk_height: float = 0.1 * au_to_m
    return np.pi * disk_radius**2 * disk_height


@njit
def find_disk_mass(stellar_mass: float) -> float:
    """Get disk mass from stellar mass

    Args:
        stellar_mass (float): Stellar mass in SI units
    Returns:
        float: Mass of disk in SI units
    """
    return 0.1 * stellar_mass


@njit
def find_dust_mass(stellar_mass: float) -> float:
    """Get dust mass from stellar mass

    Args:
        stellar_mass (float): Stellar mass in SI units
    Returns:
        float: Mass of dust in disk in SI units
    """
    return 0.01 * find_disk_mass(stellar_mass)


@njit
def find_density(disk_volume: float, stellar_mass: float) -> float:
    """Get disk density from disk volume and stellar mass

    Args:
        disk_volume (float): Volume of disk in SI units
        stellar_mass (float): Stellar mass in SI units
    Returns:
        float: Density of disk in SI units
    """
    dust_mass = find_dust_mass(stellar_mass)
    return dust_mass / disk_volume
