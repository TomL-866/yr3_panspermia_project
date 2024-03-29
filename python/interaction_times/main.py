import numpy as np
from interaction_times.collision_times import (
    t_coll_disk,
    t_coll_earth,
)
from helpers import get_base_dir
from disk_calcs.disk import DiskCalcs

AU_TO_M: float = 1.49597871e11

# https://www.doi.org/10.3847/2041-8213/aaae67 gives the
# number density of 'Oumuamua-like objects as 0.2 per cubic AU
N_O: float = 0.2 * 1 / (AU_TO_M**3)  # SI units

# https://doi.org/10.1038/nature25020 gives the
# velocity of 'Oumuamua-like object as 26 km/s.
# See also https://doi.org/10.1051/0004-6361/202141283.

# This is speed relative to the Sun.
# NOTE: https://www.nature.com/articles/s41550-019-0816-x gives a much more accurate value
V_O: float = 26e3  # SI units


def calc_coll_time_earth() -> None:
    n_o = N_O
    v_o = V_O

    collision_time = t_coll_earth(n_o, v_o)

    np.save(
        f"{get_base_dir()}/output/values/collision_time_earth.npy",
        collision_time,
    )


def calc_coll_time_disk(stellar_mass: np.ndarray, disk: DiskCalcs) -> None:
    v_o = V_O
    n_o = N_O

    collision_times_side_on, collision_times_top_down = t_coll_disk(
        n_o, v_o, disk, stellar_mass
    )

    np.save(
        f"{get_base_dir()}/output/values/collision_times_disk_sideon.npy",
        collision_times_side_on,
    )
    np.save(
        f"{get_base_dir()}/output/values/collision_times_disk_topdown.npy",
        collision_times_top_down,
    )


def main(stellar_mass: np.ndarray) -> None:
    calc_coll_time_earth()
    disk: DiskCalcs = DiskCalcs(stellar_mass)
    calc_coll_time_disk(stellar_mass, disk)
