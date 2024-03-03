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


def t_coll_disk(n_o: float, v_o: float, csa: float, disk: DiskCalcs) -> float:
    """Get collision time of 'Oumuamua-like object with dust disk

    Args:
        n_o (float): Number density of 'Oumuamua-like objects in SI units
        v_o (float): Velocity of 'Oumuamua-like object in SI units
        csa (float): Cross sectional area of disk in SI units
        disk (DiskCalcs): Disk object
    """

    stellar_mass: float = load_stellar_mass_file()
    stellar_radius: float = stellar_mass**0.8  # Mass-radius relation for MS stars

    G: float = astro_const.G.value

    v_esc_star: float = np.sqrt(2 * G * stellar_mass / stellar_radius)
    v_esc = (
        v_esc_star  # NOTE: Fix this to something more sensible - perhaps ask Richard
    )
    print("!! FIX V_ESC FOR DUST DISK !!")
    # Possible ideas:
    # https://www.sciencedirect.com/topics/earth-and-planetary-sciences/protoplanetary-disk

    C: float = csa * (1 + v_esc**2 / v_o**2)  # Collision cross section in SI units

    return 1 / (n_o * C * v_o)
