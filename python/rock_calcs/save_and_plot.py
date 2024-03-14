import numpy as np
import matplotlib.pyplot as plt
from helpers import get_base_dir


M_MOON = 7.34767309e22  # SI Units
M_LOW = 10  # SI Units
M_UPP = M_MOON


def save_rock_dist(rock_masses: np.ndarray) -> None:
    base_dir: str = get_base_dir()
    np.save(f"{base_dir}/output/values/rock_masses.npy", rock_masses)


def plot_rock_dist(rock_masses: np.ndarray) -> None:
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
    plt.xlim(np.min((rock_masses / M_MOON)), 10**0)
    plt.xlabel("Rock mass (M$_{Moon}$)")
    plt.ylabel("Frequency")
    plt.title("Rock Mass Distribution")
    plt.savefig(get_base_dir() + "/output/graphs/rock_mass_histogram.png")
    # plt.savefig(get_base_dir() + "/output/graphs/rock_mass_histogram.pgf")
    plt.close()


def save_rock_lifetimes(rock_lifetimes: np.ndarray) -> None:
    base_dir: str = get_base_dir()
    np.save(f"{base_dir}/output/values/rock_lifetimes.npy", rock_lifetimes)


def plot_rock_lifetimes(rock_radii: np.ndarray, rock_lifetimes: np.ndarray) -> None:
    days_in_a_year: float = (
        365 + 0.25 - 0.01 + 0.0025 - 0.00025
    )  # 365.2425 days for Gregorian calendar

    # # Downsample values because matplotlib chunk size limit is too small
    # rock_radii = rock_radii[::1000]
    # rock_lifetimes = rock_lifetimes[::1000]

    rock_lifetimes = np.sort(rock_lifetimes)
    rock_radii = np.sort(rock_radii)

    moon_radius: float = 1737.4 * 10**3
    # find radius where mass of rock is equal to mass of moon
    max_radius: float = (3 / (4 * np.pi)) ** (1 / 3) * moon_radius
    mask = rock_radii < max_radius

    plt.figure()
    plt.plot(
        rock_radii[mask],
        rock_lifetimes[mask] / (10**6 * days_in_a_year * 24 * 60 * 60),
        # "o",
        # markersize=1,
    )

    plt.yscale("log")
    # plt.xscale("log")
    plt.xlabel("Rock radii (m)")
    plt.ylabel("Rock lifetime (Myr)")
    plt.title("Rock Lifetime vs Radius of rock")
    plt.savefig(get_base_dir() + "/output/graphs/rock_lifetime_vs_rock_radius.png")
    # plt.savefig(get_base_dir() + "/output/graphs/rock_lifetime_vs_rock_radius.pgf")
    plt.close()
