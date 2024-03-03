import numpy as np
import os


def get_base_dir() -> str:
    """This function returns the base directory of the project"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_stellar_mass_file() -> np.ndarray:
    """This function loads the stellar mass file and returns it as a numpy array"""
    base_dir: str = get_base_dir()
    stellar_mass: str = np.load(f"{base_dir}/output/values/stellar_masses.npy")
    return stellar_mass
