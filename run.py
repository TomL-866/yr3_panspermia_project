import python.IMF.main as imf
import python.disk_calcs.main as disk
import time
from python.IMF.main import get_stellar_mass_array

if __name__ == "__main__":
    start = time.perf_counter()

    # Call get_stellar_mass_array() once
    stellar_mass_arr = get_stellar_mass_array()

    # Pass the array to the functions that need it
    imf.main(stellar_mass_arr)
    disk.main(stellar_mass_arr)

    print(f"Time taken: {time.perf_counter() - start} seconds")
