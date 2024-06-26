import matplotlib
import time
import imf.main as imf
import disk_calcs.main as disk
import interaction_times.main as interaction_times
from imf.main import get_stellar_mass_array
import rock_calcs.main as rock_calcs

if __name__ == "__main__":
    # # PGF plot settings for exporting plots to LaTeX
    # matplotlib.use("pgf")
    # matplotlib.rcParams.update(
    #     {
    #         "pgf.texsystem": "pdflatex",
    #         "font.family": "serif",
    #         "font.serif": ["Times New Roman", "CMU Serif"],  #  Fallback to CMU Serif
    #         "text.usetex": True,
    #         "pgf.rcfonts": False
    #     }
    # )

    matplotlib.rcParams.update({"font.size": 14})
    matplotlib.rcParams.update({"figure.autolayout": True})

    start = time.perf_counter()

    print("\n---PROGRAM START---")
    stellar_mass_arr = get_stellar_mass_array()

    # Calculate and plot initial mass function
    print("")
    imf.main(stellar_mass_arr)

    # Calculate disk values and plot dust mass vs disk density
    print("")
    disk.main(stellar_mass_arr)

    # Get collision time for 'Oumuamua-like object with Earth
    # and the dust disk
    print("")
    interaction_times.main(stellar_mass_arr)

    # Calculate and plot rock mass distribution
    print("")
    rock_calcs.main()

    print(f"\nProgram took {time.perf_counter() - start} s to run")
    print("---PROGRAM END---\n")
