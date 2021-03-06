import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math as mt
import numpy as np

def rotation_matrix(fi):
    """


    Parameters
    ----------
    fi : float
        angle in rad

    Returns
    -------
    2x2 numpy array
        rotation matrix

    """
    return np.array([[mt.cos(fi), -mt.sin(fi)], [mt.sin(fi), mt.cos(fi)]])

def rotation_in_place(xy_array, fi):
    """
    

    Parameters
    ----------
    xy_array : numpy array
        Nx2 numpy array of coordinates
    fi : float
        angle in degrees
    x0 : float
        x coordinate of a initial position
    y0 : float
        y coordinate of a initial position
    Returns
    -------
    xy_final : numpy array
        Nx2 array of coordinates after rotation;
        the first point is the same in both input and output arrays

    """
    fi = fi * mt.pi / 180
    xy_rot = np.dot(rotation_matrix(fi), xy_array.T).T
    dx = xy_array[0, 0] - xy_rot[0, 0]
    dy = xy_array[0, 1] - xy_rot[0, 1]
            
    xy_final = xy_rot + np.array([dx, dy])
    
    return xy_final

def smallest_distance(x_p, y_p, x_curve, y_curve):
    """


    Parameters
    ----------
    x_p : float
        x-coordinate of a point
    y_p : float
        y-coordinate of a point
    x_curve : numpy array
        x-coordinates of points describing a curve
    y_curve : numpy array
        y-coordinates of points describing a curve

    Returns
    -------
    float
        the smallest distance between the given point and curve

    """

    diff_squared_x = np.power(x_curve - x_p, 2)
    diff_squared_y = np.power(y_curve - y_p, 2)
    distances = np.sqrt(diff_squared_x + diff_squared_y)
    return distances.min()


def largest_distance(x_p, y_p, x_curve, y_curve):
    """


    Parameters
    ----------
    x_p : float
        x-coordinate of a point
    y_p : float
        y-coordinate of a point
    x_curve : numpy array
        x-coordinates of points describing a curve
    y_curve : numpy array
        y-coordinates of points describing a curve

    Returns
    -------
    float
        the largest distance between the given point and curve

    """
    diff_squared_x = np.power(x_curve - x_p, 2)
    diff_squared_y = np.power(y_curve - y_p, 2)
    distances = np.sqrt(diff_squared_x + diff_squared_y)
    return distances.max()


def indices_of_inflection_points(function_array):
    """


    Parameters
    ----------
    function_array : numpy array
        values of some function to find inflections points
        (i.e. points where the function changes its sign)

    Returns
    -------
    numpy array
        indices of inflection points

    """
    diff = np.diff(function_array)
    positives = diff >= 0
    negatives = ~positives
    indices = ((positives[:-1] & negatives[1:]) |
               (positives[1:] & negatives[:-1])).nonzero()[0]

    return np.array(indices)
