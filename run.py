from python.IMF.main import main

import time

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    print(f"Time taken: {time.perf_counter() - start} seconds")
