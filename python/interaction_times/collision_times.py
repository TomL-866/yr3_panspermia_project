import numpy as np
import astropy.constants as astro_const
from disk_calcs.disk import DiskCalcs

AU_TO_M: float = 1.49597871e11


def t_coll_earth(n_o: float, v_o: float) -> float:
    """Finds collision time of 'Oumuamua-like object with Earth

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


def t_coll_disk(
    n_o: float, v_o: float, disk: DiskCalcs, stellar_mass: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Finds collision time of 'Oumuamua-like object with a disk
    for both side and top cross sectional areas

    Args:
        n_o (float): Number density of 'Oumuamua-like objects in SI units
        v_o (float): Velocity of 'Oumuamua-like object in SI units
        disk (DiskCalcs): Disk object
        stellar_mass (np.ndarray): Stellar mass array (SI)

    Returns:
        np.ndarray: Collision time in SI units for side cross sectional area
        np.ndarray: Collision time in SI units for top cross sectional area
    """
    disk_mass: np.ndarray = disk.get_mass()
    disk_radius: np.ndarray = disk.get_reduced_radius()

    csa_sideview: np.ndarray = disk.get_csa_sideview()
    csa_topview: np.ndarray = disk.get_csa_topview()

    G: float = astro_const.G.value

    v_esc: float = np.sqrt(2 * G * (stellar_mass + disk_mass) / disk_radius)

    C_side: float = csa_sideview * (1 + v_esc**2 / v_o**2)
    C_top: float = csa_topview * (1 + v_esc**2 / v_o**2)

    return 1 / (n_o * C_side * v_o), 1 / (n_o * C_top * v_o)
