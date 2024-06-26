import astropy.constants as astro_const
import numpy as np


def si_to_msun_au3(density: np.ndarray) -> np.ndarray:
    """Converts density from SI (kg/m^3) to Msun/AU^3

    Args:
        density (np.ndarray): Density in SI units (kg/m^3)
    Returns:
        np.ndarray: Density in Msun/AU^3
    """
    au_to_m: float = astro_const.au.value
    m_sun: float = astro_const.M_sun.value
    return density * (au_to_m**3) / m_sun


def si_to_msun_pc3(density: np.ndarray) -> np.ndarray:
    """Converts density from SI (kg/m^3) to Msun/pc^3

    Args:
        density (np.ndarray): Density in SI units (kg/m^3)
    Returns:
        np.ndarray: Density in Msun/pc^3
    """
    pc_to_m: float = astro_const.pc.value
    m_sun: float = astro_const.M_sun.value
    return density * (pc_to_m**3) / m_sun


def si_to_g_cm3(density: np.ndarray) -> np.ndarray:
    """Converts density from SI (kg/m^3) to g/cm^3
    
    Args:
        density (np.ndarray): Density in SI units (kg/m^3)
    Returns:
        np.ndarray: Density in Msun/pc^3
    """
    return density / 1000
