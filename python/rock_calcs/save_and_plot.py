import numpy as np
import matplotlib.pyplot as plt
from helpers import get_base_dir

# All consts are in SI units
M_MOON = 7.34767309e22
M_LOW = 10
M_UPP = M_MOON


def save_rock_dist(rock_masses: np.ndarray) -> None:
    """Saves the rock masses to a .npy file in the output/values directory.

    Args:
        rock_masses (np.ndarray): Rock masses array
    """
    base_dir: str = get_base_dir()
    np.save(f"{base_dir}/output/values/rock_masses.npy", rock_masses)


def plot_rock_dist(rock_masses: np.ndarray) -> None:
    """Plots the rock mass distribution as a histogram

    Args:
        rock_masses (np.ndarray): Rock masses array
    """
    plt.figure()
    bins: list[float] = list(
        np.logspace(np.log10(M_LOW / M_MOON), np.log10(M_UPP / M_MOON), num=500)
    )
    plt.hist(
        rock_masses / M_MOON,
        bins=bins,
    )
    plt.yscale("log")
    plt.xscale("log")
    plt.xlim(np.min(rock_masses) / M_MOON, 10**0)
    plt.xlabel("Rock mass (M$_{Moon}$)")
    plt.ylabel("Frequency")
    plt.title("Rock Mass Distribution")
    plt.savefig(get_base_dir() + "/output/graphs/rock_mass_histogram.png")
    # plt.savefig(get_base_dir() + "/output/graphs/rock_mass_histogram.pgf")
    plt.close()


def save_rock_lifetimes(rock_lifetimes: np.ndarray) -> None:
    """Saves the rock lifetimes to a .npy file in the output/values directory.

    Args:
        rock_lifetimes (np.ndarray): Rock lifetimes array
    """
    base_dir: str = get_base_dir()
    np.save(f"{base_dir}/output/values/rock_lifetimes.npy", rock_lifetimes)


def plot_rock_lifetimes(rock_radii: np.ndarray, rock_lifetimes: np.ndarray) -> None:
    """Plots the rock lifetimes as a function of rock radius

    Args:
        rock_radii (np.ndarray): Rock radii array
        rock_lifetimes (np.ndarray): Rock lifetime array
    """
    days_in_a_year: float = 365 + 0.25 - 0.01 + 0.0025 - 0.00025

    rock_lifetimes = np.sort(
        rock_lifetimes
    )  # Need to sort so matplotlib plots in order
    rock_radii = np.sort(rock_radii)
    rock_density: float = 4 * 1e3  # SI

    # find radius where mass of rock is equal to mass of moon
    max_radius: float = np.max(
        rock_radii[np.where(4 / 3 * np.pi * rock_radii**3 * rock_density <= M_MOON)]
    )
    mask = rock_radii < max_radius

    plt.figure()
    plt.plot(
        rock_radii[mask],
        rock_lifetimes[mask] / (10**6 * days_in_a_year * 24 * 60 * 60),
    )

    plt.yscale("log")
    # plt.xscale("log")
    plt.xlabel("Rock radii (m)")
    plt.ylabel("Rock lifetime (Myr)")
    plt.title("Rock Lifetime vs Radius of rock")
    plt.savefig(get_base_dir() + "/output/graphs/rock_lifetime_vs_rock_radius.png")
    # plt.savefig(get_base_dir() + "/output/graphs/rock_lifetime_vs_rock_radius.pgf")
    plt.close()
