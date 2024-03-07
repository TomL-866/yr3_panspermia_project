import numpy as np
from interaction_times.equations import t_coll_disk, t_coll_earth
from helpers import get_base_dir
from disk_calcs.disk import DiskCalcs


def calc_coll_time_earth() -> None:
    au_to_m: float = 1.49597871e11

    # https://www.doi.org/10.3847/2041-8213/aaae67 gives the
    # number density of 'Oumuamua-like objects as 0.2 per cubic AU
    n_o: float = 0.2 * 1 / (au_to_m**3)  # SI units

    # https://doi.org/10.1038/nature25020 gives the
    # velocity of 'Oumuamua-like object as 26 km/s.
    # See also https://doi.org/10.1051/0004-6361/202141283.

    # This is speed relative to the Sun.
    # NOTE: https://www.nature.com/articles/s41550-019-0816-x gives a much more accurate value
    v_o: float = 26e3  # SI units

    days_in_a_year: float = (
        365 + 0.25 - 0.01 + 0.0025 - 0.00025
    )  # 365.2425 days for Gregorian calendar

    collision_time = t_coll_earth(n_o, v_o)

    print(
        f"Time for collision between 'Oumuamua and Earth: {collision_time / (days_in_a_year * 24 * 60 * 60 * 1e6)} Myr"
    )

    np.save(
        f"{get_base_dir()}/output/values/collision_time_earth.npy",
        collision_time,
    )


def calc_coll_time_disk(disk: DiskCalcs) -> None:
    au_to_m: float = 1.49597871e11

    # https://www.doi.org/10.3847/2041-8213/aaae67 gives the
    # number density of 'Oumuamua-like objects as 0.2 per cubic AU
    n_o: float = 0.2 * 1 / (au_to_m**3)  # SI units

    # https://doi.org/10.1038/nature25020 gives the
    # velocity of 'Oumuamua-like object as 26 km/s.
    # See also https://doi.org/10.1051/0004-6361/202141283.

    # This is speed relative to the Sun.
    v_o: float = 26e3  # SI units

    # days_in_a_year: float = (
    #     365 + 0.25 - 0.01 + 0.0025 - 0.00025
    # )  # 365.2425 days for Gregorian calendar

    csa_side_on: float = disk.get_csa_sideview()
    csa_top_down: float = disk.get_csa_topview()

    collision_time_side_on: float = t_coll_disk(n_o, v_o, csa_side_on, disk)
    collision_time_top_down: float = t_coll_disk(n_o, v_o, csa_top_down, disk)

    np.save(
        f"{get_base_dir()}/output/values/collision_times_disk_sideon.npy",
        collision_time_side_on,
    )
    np.save(
        f"{get_base_dir()}/output/values/collision_times_disk_topdown.npy",
        collision_time_top_down,
    )


def main(stellar_mass: np.ndarray) -> None:
    calc_coll_time_earth()
    disk = DiskCalcs(stellar_mass)
    calc_coll_time_disk(disk)
