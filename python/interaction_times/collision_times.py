import numpy as np
import astropy.constants as astro_const
from disk_calcs.disk import DiskCalcs
from helpers import load_stellar_mass_file


def t_coll_earth(n_o: float, v_o: float) -> float:
    """Get collision time of 'Oumuamua-like object with Earth

    Args:
        n_o (float): Number density of 'Oumuamua-like objects in SI units
        v_o (float): Velocity of 'Oumuamua-like object in SI units
    Returns:
        float: Collision time in SI units
    """
    r_earth: float = astro_const.R_earth.value
    m_earth: float = astro_const.M_earth.value
    G: float = astro_const.G.value

    v_esc: float = np.sqrt(2 * G * m_earth / r_earth)
    C: float = (
        np.pi * r_earth**2 * (1 + v_esc**2 / v_o**2)
    )  # Collision cross section in SI units
    return 1 / (n_o * C * v_o)


def t_coll_disk(n_o: float, v_o: float, csa: float, disk: DiskCalcs) -> np.ndarray:
    """Get collision time of 'Oumuamua-like object with dust disk

    Args:
        n_o (float): Number density of 'Oumuamua-like objects in SI units
        v_o (float): Velocity of 'Oumuamua-like object in SI units
        csa (float): Cross sectional area of disk in SI units
        disk (DiskCalcs): Disk object

    Returns:
        np.ndarray: Collision times for 'Oumuamua for each disk 
    """

    stellar_mass: np.ndarray = load_stellar_mass_file()
    stellar_radius: np.ndarray = stellar_mass**0.8  # Mass-radius relation for MS stars

    disk_mass: np.ndarray = disk.get_mass()
    disk_radius: np.ndarray = disk.get_radius()

    G: float = astro_const.G.value

    v_esc: float = np.sqrt(
        2 * G * (stellar_mass + disk_mass) / (stellar_radius + disk_radius)
    )

    C: float = csa * (1 + v_esc**2 / v_o**2)  # Collision cross section in SI units

    return 1 / (n_o * C * v_o)
