import numpy as np


def rock_mass_to_radius(rock_masses: np.ndarray) -> np.ndarray:
    """Converts rock masses to radii using rock density.

    Args:
        rock_masses (np.ndarray): Rock mass array

    Returns:
        np.ndarray: Rock radii array
    """
    rock_density_cgs = 4  # g/cm^3
    rock_density = rock_density_cgs * 10 ** (-3) * 1 / (10 ** (-6))

    return (3 * rock_masses / (4 * np.pi * rock_density)) ** (1 / 3)


def rock_radius_to_lifetime(rock_radii: np.ndarray) -> np.ndarray:
    """Converts rock radius to lifetime using the formula t = 75 * r^2.
    This comes from https://doi.org/10.1088/0004-637X/690/1/210.

    Args:
        rock_radii (np.ndarray): Rock radii array

    Returns:
        np.ndarray: Rock lifetime array
    """
    t_myr = 75 * rock_radii**2

    days_in_a_year: float = (
        365 + 0.25 - 0.01 + 0.0025 - 0.00025
    )  # 365.2425 days for Gregorian calendar

    t = t_myr * 10**6 * days_in_a_year * 24 * 60 * 60  # SI units
    return t
