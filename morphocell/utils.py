import math


def euclidean_distance(point_x, point_y):
    """
    Method to calculate euclidean distance between two points in n-dimensions.
    Both points must have the same dimensions
    """
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(point_x, point_y)]))
