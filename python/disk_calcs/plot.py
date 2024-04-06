import numpy as np
import matplotlib.pyplot as plt


def plot_disk_radii_dist(disk_radii: np.ndarray) -> None:
    plt.figure()
    plt.hist(disk_radii, bins=75)
    plt.yscale("log")
    plt.xscale("log")
    plt.xlim(np.min(disk_radii), np.max(disk_radii))
    plt.xlabel("Disk radii (m)")
    plt.ylabel("Frequency")
    plt.savefig("output/graphs/disk_radii_histogram.png")
    plt.close()
