import matplotlib
import IMF.main as imf
import disk_calcs.main as disk
import interaction_times.main as interaction_times
import time
from IMF.main import get_stellar_mass_array


if __name__ == "__main__":
    # PGF plot settings for exporting plots to LaTeX
    # matplotlib.use("pgf")
    # matplotlib.rcParams.update(
    #     {
    #         "pgf.texsystem": "xelatex",  # Or "lualatex"
    #         "font.family": "serif",
    #         "font.serif": [],  # Avoid redundancy
    #         "text.usetex": True,
    #         "pgf.rcfonts": False,
    #         "pgf.preamble": r"\usepackage{fontspec}\setmainfont{Times New Roman}",
    #     }
    # )

    start = time.perf_counter()

    print("\n---PROGRAM START---")
    stellar_mass_arr = get_stellar_mass_array()

    # Calculate and plot initial mass function
    imf.main(stellar_mass_arr)

    # Calculate disk values and plot dust mass vs disk density
    disk.main(stellar_mass_arr)

    # Get collision time for 'Oumuamua-like object with Earth
    interaction_times.main()

    print(f"Program took {time.perf_counter() - start} s to run")
    print("---PROGRAM END---\n")
