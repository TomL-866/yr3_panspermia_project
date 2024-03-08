import numpy as np
import matplotlib.pyplot as plt
from rock_calcs.mass_dist import rock_dist
from helpers import get_base_dir

RUNS = 1_000_000
M_MOON = 7.34767309e22  # SI Units
M_LOW = 10  # SI Units
M_UPP = M_MOON


def get_rock_dist() -> np.ndarray:
    """This function generates a rock mass distribution

    Returns:
        np.ndarray: Rock mass distribution in kg
    """
    u: float = np.random.uniform(0, 1, RUNS)

    return rock_dist(u)


def save_rock_dist() -> None:
    base_dir: str = get_base_dir()
    np.save(f"{base_dir}/output/values/rock_masses.npy", get_rock_dist())


def plot_rock_dist() -> None:
    plt.figure()
    bins: list[float] = list(np.logspace(np.log10(M_LOW), np.log10(M_UPP), num=75))
    plt.hist(
        get_rock_dist() / M_MOON,
        bins=bins,
    )
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("Rock mass (M$_{Moon}$)")
    plt.ylabel("Frequency")
    plt.title("Rock Mass Distribution")
    plt.savefig(get_base_dir() + "/output/graphs/rock_mass_histogram.png")
    # plt.savefig(get_base_dir() + "/output/graphs/rock_mass_histogram.pgf")
    plt.close()


def main() -> None:
    print("Generating rock mass distribution...")
    save_rock_dist()
    print("Plotting rock mass distribution...")
    plot_rock_dist()
