from numba import njit
import astropy.constants as astro_const

P = 1.8
M_MOON = 7.34767309e22  # SI Units
M_UPP = M_MOON
M_LOW = 10  # SI Units
M_EARTH = astro_const.M_earth.value  # SI Units


@njit
def rock_dist(u: float) -> float:
    """This function generates a mass distribution of rocks,
    rocks being the type of rock 'Oumuamua is thought to be.

    Args:
        u (float): Random number between 0 and 1

    Returns:
        float: Rock mass in kg
    """
    m_R = M_EARTH
    m_2 = 0.1 * M_EARTH
    A = (
        (2 - P) * m_R / m_2 ** (2 - P)
    )  # Constant from Equation 7 in Adams and Napier 2022
    return A * (u * M_UPP ** (1 - P) + (1 - u) * M_LOW ** (1 - P)) ** (1 / (1 - P))
