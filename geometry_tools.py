'''module for computing areas, moments, baricenters etc...'''
import numpy as np


def compute_area(points):
    '''computes the area of a simply connected shape using
    the Green theorem.
    Right now it assumes the shape is closed, i.e., the last point
    is "joined" with the first one.
    '''
    x, y = points
    F_x = -y/2
    F_y =  x/2

    dx = np.diff(x)
    dy = np.diff(y)

    A = np.sum( F_x[1:] * dx + F_y[1:] * dy)

    return np.abs(A)
