import numpy as np
import os


def get_base_dir() -> str:
    """Returns the base directory of the project.
    This is the directory that contains the `python` directory.

    Returns:
        str: The base directory of the project.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_stellar_mass_file() -> np.ndarray:
    """This function returns the array of stellar masses
    by loading the .npy file from the output/values directory.

    Returns:
        np.ndarray: Stellar masses array (SI)
    """
    base_dir: str = get_base_dir()
    stellar_mass: str = np.load(f"{base_dir}/output/values/stellar_masses.npy")
    return stellar_mass
