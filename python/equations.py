"""This module contains functions representing equations in https://doi.org/10.1093/mnras/sts479"""

import astropy.constants as astro_const


def quantile_func(u: float) -> float:
    """This function replicates the quantile function,
    Equation 4 in Table 1 of https://doi.org/10.1093/mnras/sts479.
    Values of constants are taken directly from the paper,
    except from the upper and lower mass limits.

    Args:
        u (float): Random number between 0 and 1

    Returns:
        float: Result of quantile function, which is a stellar mass in SI units.
    """

    mu: float = 0.2 * astro_const.M_sun.value
    alpha: float = 2.3
    beta: float = 1.4

    upper_mass_limit: float = 50 * astro_const.M_sun.value
    lower_mass_limit: float = 0.1 * astro_const.M_sun.value

    return mu * (
        (
            u * (auxiliary_func(upper_mass_limit) - auxiliary_func(lower_mass_limit))
            + auxiliary_func(lower_mass_limit)
        )
        ** (1 / (1 - beta))
        - 1
    ) ** (1 / (1 - alpha))


def auxiliary_func(stellar_mass: float) -> float:
    """This function replicates the auxiliary function,
    Equation 1 in Table 1 of https://doi.org/10.1093/mnras/sts479.
    Values of constants are taken directly from the paper.

    Args:
        stellar_mass (float): Stellar mass (SI units)

    Returns:
        float: Result of auxiliary function (SI units)
    """

    mu: float = 0.2 * astro_const.M_sun.value
    alpha: float = 2.3
    beta: float = 1.4

    return (1 + (stellar_mass / mu) ** (1 - alpha)) ** (1 - beta)
