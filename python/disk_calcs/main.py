import numpy as np
from disk_calcs.disk import DiskCalcs


def main(stellar_mass: np.ndarray) -> None:
    DiskCalcs(stellar_mass).run()
