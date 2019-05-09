import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist


def get_distances(data, point):
    """ Calculate the distance between the data set and a specific point """
    return cdist(data, point.reshape((-1, 1)).T)[:, 0]


def calc_mean_and_basin(data, point, r, c):
    """
    Calculate the mean point in the circle with center "point" and radius "r"
    :param data: n-dimensional dataset containing p points
    :param point: center of the circle of search
    :param r: radius of the circle
    :param c: radius of the circle for the basin of attraction
    :return: mean point, basin of attraction
    """
    distances = get_distances(data, point)
    mean_point = np.mean(data[distances < r, :], axis=0)

    distances_to_mean = get_distances(data, mean_point)
    basin_of_attraction = np.argwhere(distances_to_mean < r / c)[:, 0]

    return mean_point, basin_of_attraction


def plot_clusters_3d(data, labels, peaks, r):
    """
    Plots the modes of the given image data in 3D by coloring each pixel
    according to its corresponding peak.
    Args:
        data: image data in the format [number of pixels]x[feature vector].
        labels: a list of labels, one for each pixel.
        peaks: a list of vectors, whose first three components can
        be interpreted as RGB values.
        r: radius used for the clustering
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    colors = np.random.uniform(0, 1, (len(peaks), 3))

    for idx, peak in enumerate(peaks):
        cluster = data[np.where(labels == idx)[0]].T
        ax.scatter(cluster[0], cluster[1], cluster[2], c=[colors[idx]], s=.5, label="Group =" + str(idx))

    plt.title("radius = " + str(r))
    plt.legend(markerscale=10)
    plt.show()
