import numpy as np
import astropy.constants as astro_const
import matplotlib.pyplot as plt
import pandas as pd
from helpers import get_base_dir, sig_figs
import rust

# All consts are in SI units
M_MOON = 7.34767309e22
M_LOW = 10
M_UPP = M_MOON
R_MOON = 1.7371e6


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
    bins: list[float] = list(np.logspace(np.log10(M_LOW), np.log10(M_UPP), num=75))
    plt.hist(
        rock_masses,  # / M_MOON,
        bins=bins,
    )
    plt.yscale("log")
    plt.xscale("log")
    plt.xlim(M_LOW, np.max(rock_masses))
    print(f"MAX ROCK MASS: {np.max(rock_masses)}")
    plt.xlabel("Rock mass (kg)")
    plt.ylabel("Frequency")
    # plt.title("Rock Mass Distribution")
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

    mask = np.where(rock_radii <= R_MOON)  # densities are very similar

    plt.figure()
    plt.plot(
        rock_radii[mask],
        rock_lifetimes[mask] / (10**6 * days_in_a_year * 24 * 60 * 60),
    )
    # plot horizontal line showing the age of the universe
    age_of_universe_myr = 13.787e3
    plt.hlines(
        age_of_universe_myr,
        rock_radii[0],
        rock_radii[-1],
        colors="r",
        linestyles="--",
        label="Age of the Universe",
    )

    plt.yscale("log")
    # plt.xscale("log")
    plt.xlabel("Rock radii (m)")
    plt.ylabel("Rock lifetime (Myr)")
    # plt.title("Rock Lifetime vs Radius of rock")
    plt.savefig(get_base_dir() + "/output/graphs/rock_lifetime_vs_rock_radius.png")
    # plt.savefig(get_base_dir() + "/output/graphs/rock_lifetime_vs_rock_radius.pgf")
    plt.close()


def extract_colltimes() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    # earth_coll_times is a dictionary of a dictionary.
    # The first key is n_o, the second key is v_o.
    # The value is the collision time.
    earth_coll_times = rust.return_coll_times()[0]

    # n_o_keys_earth = earth_coll_times.keys()
    # v_o_keys_earth = earth_coll_times[list(n_o_keys_earth)[0]].keys()
    # collision_times_earth_forloop = []
    # for n_o in n_o_keys_earth:
    #     for v_o in v_o_keys_earth:
    #         collision_times_earth_forloop.append(earth_coll_times[n_o][v_o])

    earth_df = pd.DataFrame(
        [
            (n_o, v_o, time)
            for n_o, v_o_dict in earth_coll_times.items()
            for v_o, time in v_o_dict.items()
        ],
        columns=["n_o", "v_o", "coll_time"],
    )

    # disk_coll_times_side is a dictionary of a dictionary of a dictionary.
    # The first key is a stellar mass, the second key is n_o, the third key is v_o.
    # The value is the collision time.
    disk_coll_times_side = rust.return_coll_times()[1]

    # stellar_keys_side = disk_coll_times_side.keys()
    # n_o_keys_side = disk_coll_times_side[list(stellar_keys_side)[0]].keys()
    # v_o_keys_side = disk_coll_times_side[list(stellar_keys_side)[0]][
    #     list(n_o_keys_side)[0]
    # ].keys()
    # collision_times_disk_side = []
    # for stellar_mass in stellar_keys_side:
    #     for n_o in n_o_keys_side:
    #         for v_o in v_o_keys_side:
    #             collision_times_disk_side.append(
    #                 disk_coll_times_side[stellar_mass][n_o][v_o]
    #             )

    side_df = pd.DataFrame(
        [
            (stellar_mass, n_o, v_o, time)
            for stellar_mass, n_o_dict in disk_coll_times_side.items()
            for n_o, v_o_dict in n_o_dict.items()
            for v_o, time in v_o_dict.items()
        ],
        columns=["stellar_mass", "n_o", "v_o", "coll_time"],
    )

    # disk_coll_times_top is a dictionary of a dictionary of a dictionary.
    # The first key is a stellar mass, the second key is n_o, the third key is v_o.
    # The value is the collision time.
    disk_coll_times_top = rust.return_coll_times()[2]

    # stellar_keys_top = disk_coll_times_top.keys()
    # n_o_keys_top = disk_coll_times_top[list(stellar_keys_top)[0]].keys()
    # v_o_keys_top = disk_coll_times_top[list(stellar_keys_top)[0]][
    #     list(n_o_keys_top)[0]
    # ].keys()
    # collision_times_disk_top = []
    # for stellar_mass in stellar_keys_top:
    #     for n_o in n_o_keys_top:
    #         for v_o in v_o_keys_top:
    #             collision_times_disk_top.append(
    #                 disk_coll_times_top[stellar_mass][n_o][v_o]
    #             )

    top_df = pd.DataFrame(
        [
            (stellar_mass, n_o, v_o, time)
            for stellar_mass, n_o_dict in disk_coll_times_top.items()
            for n_o, v_o_dict in n_o_dict.items()
            for v_o, time in v_o_dict.items()
        ],
        columns=["stellar_mass", "n_o", "v_o", "coll_time"],
    )

    return earth_df, side_df, top_df


def earth_lifetime_coll_time_plot(earth_df, colors) -> None:
    v_o_full = np.unique(earth_df["v_o"])
    n_o_full = np.unique(earth_df["n_o"])

    plt.figure()
    plt.yticks(
        v_o_full,  # Positions
        [1, 5, 10, 20, 30],  # Labels (v_o in km/s)
    )
    plt.xlabel("Collision time with Earth (Myr)")
    plt.ylabel("v$_o$ (km/s)")

    for i, v_o in enumerate(v_o_full):
        for j, n_o in enumerate(n_o_full):
            coll_times = earth_df.loc[
                (earth_df["v_o"] == v_o) & (earth_df["n_o"] == n_o)
            ]["coll_time"].to_numpy()

            if i == 0:
                plt.scatter(
                    coll_times / (10**6 * 365.25 * 24 * 60 * 60),
                    v_o_full[i],
                    color=colors[j],
                    label=f"n$_o$ = {sig_figs(n_o * astro_const.au.value**3, 1)} AU$^{{-3}}$",
                )
            plt.scatter(
                coll_times / (10**6 * 365.25 * 24 * 60 * 60),
                v_o_full[i],
                color=colors[j],
            )
    # Plot dotted line that represents maximum rock survival time
    rock_survival_times = np.load(f"{get_base_dir()}/output/values/rock_lifetimes.npy")

    print("Summary statistics for rock survival times:")
    disk_sideon_df = pd.DataFrame(
        rock_survival_times / (365.25 * 24 * 60 * 60 * 10**6),
        columns=["Survival Time (Myr)"],
    )
    print(disk_sideon_df.describe())
    print(f"median: {disk_sideon_df.median()}")

    plt.axvline(
        x=np.max(rock_survival_times) / (10**6 * 365.25 * 24 * 60 * 60),
        color="black",
        linestyle="--",
        label="Maximum rock survival time",
    )
    plt.axvline(
        np.median(rock_survival_times) / (10**6 * 365.25 * 24 * 60 * 60),
        color="orange",
        linestyle="--",
        label="Median rock survival time",
    )
    plt.axvline(
        np.min(rock_survival_times) / (10**6 * 365.25 * 24 * 60 * 60),
        color="purple",
        linestyle="--",
        label="Minimum rock survival time",
    )

    plt.legend()
    plt.xscale("log")
    plt.savefig(get_base_dir() + "/output/graphs/lifetime_vs_coll_times.png")


import matplotlib.patches as mpatches


def disk_lifetime_coll_time_plot(disk_df, colors, view) -> None:
    n_o_full = np.unique(disk_df["n_o"])

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    color_dict = {n_o: colors[i] for i, n_o in enumerate(n_o_full)}
    color_values = disk_df["n_o"].map(color_dict)

    ax.scatter(
        np.log10(disk_df["coll_time"] / (10**6 * 365.25 * 24 * 60 * 60)),
        disk_df["v_o"] / 1e3,
        disk_df["stellar_mass"],
        c=color_values,
    )

    patches = [
        mpatches.Patch(
            color=color,
            label=f"n$_o$ = {sig_figs(n_o * astro_const.au.value**3, 1)} AU$^{{-3}}$",
        )
        for n_o, color in color_dict.items()
    ]
    ax.legend(handles=patches)
    ax.set_xlabel(f"log$_{{10}}$ of Collision time with disk's {view} (Myr)")
    ax.set_ylabel("v$_o$ (km/s)")
    ax.set_zlabel("Stellar mass (M$_\odot$)")
    plt.savefig(
        f"{get_base_dir()}/output/graphs/lifetime_vs_coll_times_disk_{view}.png"
    )
    plt.close()


def plot_lifetime_vs_coll_times() -> None:
    earth_df, side_df, top_df = extract_colltimes()

    colors = [
        "#000000",
        "#E69F00",
        "#56B4E9",
        "#009E73",
        "#F0E442",
    ]  # Colour-blind-friendly colours

    earth_lifetime_coll_time_plot(earth_df, colors)
    disk_lifetime_coll_time_plot(side_df, colors, "side")
    disk_lifetime_coll_time_plot(top_df, colors, "top")
