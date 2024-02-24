import IMF.main as imf
import disk_calcs.main as disk
import interaction_times.main as interaction_times
import time
from IMF.main import get_stellar_mass_array


if __name__ == "__main__":
    start = time.perf_counter()

    print("\n---PROGRAM START---")
    # Call get_stellar_mass_array() once
    stellar_mass_arr = get_stellar_mass_array()

    # Pass the array to the functions that need it
    imf.main(stellar_mass_arr)
    disk.main(stellar_mass_arr)

    # Get collision time for 'Oumuamua-like object with Earth
    interaction_times.main()

    print(f"Program took {time.perf_counter() - start} s to run")
    print("---PROGRAM END---\n")
