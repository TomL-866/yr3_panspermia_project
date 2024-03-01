import numpy as np
from interaction_times.equations import t_coll
from helpers import get_base_dir


def main() -> None:
    au_to_m: float = 1.49597871e11

    # https://www.doi.org/10.3847/2041-8213/aaae67 gives the number density of 'Oumuamua-like objects as 0.2 per cubic AU
    n_o: float = 0.2 * 1 / (au_to_m**3)  # SI units

    # https://doi.org/10.1038/nature25020 gives the velocity of 'Oumuamua-like object as 26 km/s
    # see also https://doi.org/10.1051/0004-6361/202141283
    # This is speed relative to the Sun.
    v_o: float = 26e3  # SI units

    days_in_a_year: float = (
        365 + 0.25 - 0.01 + 0.0025 - 0.00025
    )  # 365.2425 days for Gregorian calendar

    collision_time = t_coll(n_o, v_o)

    print(
        f"Time for collision between 'Oumuamua and Earth: {collision_time / (days_in_a_year * 24 * 60 * 60 * 1e6)} Myr"
    )

    # Write the collision time to file
    np.save(
        f"{get_base_dir()}/output/values/collision_time_w_earth.npy", collision_time
    )
