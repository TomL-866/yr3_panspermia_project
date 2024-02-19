import numpy as np
from disk_calcs.disk import Disk


def main(stellar_mass_arr: np.ndarray) -> None:
    """Main function"""

    print("Plotting dust mass vs disk density...")
    Disk().run(stellar_mass_arr)
