import numpy as np
from numba import njit


@njit
def find_radius(stellar_mass: float) -> float:
    """Get disk radius from stellar mass

    Returns:
        float: Radius of disk
    """
    au_to_m: float = 1.49597871e11
    m_sun: float = 1.98840987e30  # SI units
    return 200 * au_to_m * (stellar_mass / m_sun) ** (0.3)


@njit
def find_volume(disk_radius: float) -> float:
    """Get volume from disk radius and height

    Returns:
        float: Volume of disk
    """
    au_to_m: float = 1.49597871e11
    disk_height: float = 0.1 * au_to_m

    return np.pi * disk_radius**2 * disk_height


@njit
def find_disk_mass(stellar_mass: float) -> float:
    """Get disk mass from stellar mass

    Returns:
        float: Mass of disk
    """
    return 0.1 * stellar_mass


@njit
def find_dust_mass(stellar_mass: float) -> float:
    """Get dust mass from stellar mass

    Returns:
        float: Mass of dust
    """
    return 0.01 * find_disk_mass(stellar_mass)


@njit
def find_density(disk_volume: float, stellar_mass: float) -> float:
    """Get density from disk volume and stellar mass

    Returns:
        float: Density of disk
    """
    disk_mass = find_disk_mass(stellar_mass)
    return disk_mass / disk_volume
