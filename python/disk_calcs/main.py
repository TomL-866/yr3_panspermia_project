import numpy as np
from disk_calcs.disk import DiskCalcs


def main(stellar_mass: np.ndarray) -> None:
    """Main function"""

    print("Plotting dust mass vs disk density...")
    DiskCalcs(stellar_mass).run()
