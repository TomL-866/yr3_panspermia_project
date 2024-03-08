import numpy as np
from rock_calcs.save_and_plot import (
    save_rock_dist,
    plot_rock_dist,
    save_rock_lifetimes,
    plot_rock_lifetimes,
)
from rust import get_rock_masses
from rock_calcs.conversions import rock_mass_to_radius, rock_radius_to_lifetime


def get_rock_dist() -> np.ndarray:
    """This function generates a rock mass distribution

    Returns:
        np.ndarray: Rock mass distribution in kg
    """
    rock_masses: np.ndarray = np.array(get_rock_masses(), dtype=np.float64)
    return rock_masses


def main() -> None:
    print("Calculating rock masses...")
    rock_masses: np.ndarray = get_rock_dist()

    print("Saving rock mass distribution...")
    save_rock_dist(rock_masses)
    print("Plotting rock mass distribution...")
    plot_rock_dist(rock_masses)

    rock_radii = rock_mass_to_radius(rock_masses)
    rock_lifetimes = rock_radius_to_lifetime(rock_radii)

    print("Saving rock lifetimes...")
    save_rock_lifetimes(rock_lifetimes)
    print("Plotting rock lifetimes...")
    plot_rock_lifetimes(rock_radii, rock_lifetimes)
