import numpy as np
from disk_calcs.disk import DiskCalcs
from disk_calcs.plot import plot_disk_radii_dist


def main(stellar_mass: np.ndarray) -> None:
    disk_set = DiskCalcs(stellar_mass)
    disk_set.run()
    plot_disk_radii_dist(disk_set.get_reduced_radius())
