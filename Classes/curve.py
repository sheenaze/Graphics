import numpy as np
import math as mt
from functions import *


class Curve:

    def get_dist(self, x=None, y=None):
        """

        Returns
        -------
        numpy array
        distances between consecutive points given by pairs of coordinates;
        the first value is 0

        """
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        len_x = np.shape(x)[0]
        len_y = np.shape(y)[0]

        if len_x != len_y:
            print('x and y have different lengths')
            return
        else:
            length = [0]
            for ind in range(0, len_x - 1):
                length.append(mt.sqrt((x[ind + 1] - x[ind])
                                      ** 2 + (y[ind + 1] - y[ind])**2))
            return np.array(length)

    def get_dist_from_beginning(self, x=None, y=None):
        """

        Returns
        -------
        numpy array
        length of a curve at each given point

        """
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        distances = self.get_dist(x, y)
        if distances is not None:
            dist = []
            d = 0
            for element in distances:
                d += element
                dist.append(d)
            return np.array(dist)
        else:
            return

    def get_curve(self, x=None, y=None):
        """

        Returns
        -------
        float
        length of a curve given by points coordinates x and y

        """
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        distances = self.get_dist(x, y)
        if distances is not None:
            return np.sum(distances)
        else:
            return

    def get_ends_of_segments(self, x=None, y=None):
        """

        Returns
        -------
        numpy array
        vector of indices of points at which the particular curve segment finishes

        """
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        number_of_pieces = self.number_of_pieces
        distances = self.get_dist_from_beginning(x, y)
        curve_length = self.get_curve(x, y)

        if curve_length is not None and distances is not None:
            distances = np.round(distances, 12)
            piece_length = curve_length / number_of_pieces
            indices = []
            for n in range(1, number_of_pieces + 1):
                indices.append(
                    np.where(distances <= round(n * piece_length, 12))[0][-1])

            return np.array(indices)

        else:
            return

    def get_nominal_percentage(self, amount=500):
        """

        Returns
        -------
        numpy array
        nominal percentage of points corresponding to equal-length segments of the curve (assuming
        a large number of points)

        """
        new_x = self.new_x(self.number_of_pieces * amount)
        new_y = self.new_y(self.number_of_pieces * amount)
        length = new_x.size
        indices = self.get_ends_of_segments(new_x, new_y)
        if indices is not None:
            indices = np.insert(indices, 0, 0)
            percentage = np.diff(indices) / length * 100
            return np.round(percentage)
        else:
            return

    def get_nominal_ends(self):
        """

        Returns
        -------
        numpy array
            indices of points corresponding to ends of equal-length segments of the curve

        """
        perc = self.get_nominal_percentage()
        cum_perc = np.insert(np.cumsum(perc), 0, 0)
        indices = cum_perc / 100 * self.length
        # subtracting 1, because 100% = length and the last index is length-1
        indices[-1] = indices[-1] - 1
        return indices.astype('int')

    def horizontal_stripes(self, stripes_number):
        """

        Parameters
        ----------
        stripes_number : int
            number of horizontal stripes for area enclosed by the curve to be divided

        Returns
        -------
        numpy array
            array with indices of points which enclose each strip

        Remark: this method has been tested for a heart curve only;
                numbers of strips depends on nubers of points building the figure

        """
        x = self.x
        y = self.y
        y_max = y.max()
        y_min = y.min()
        y_vector = np.linspace(y_max, y_min, stripes_number)
        indices = []
        for i in range(y_vector.size - 1):
            inds = np.where((y <= y_vector[i]) & (y >= y_vector[i + 1]))[0]
            inds = np.insert(inds, 0, inds[0] - 1)
            if x.size - 1 not in inds:
                inds = np.append(inds, inds[-1] + 1)

            ind_inf_points = indices_of_inflection_points(y[inds])
            inf_points_num = ind_inf_points.size
            if inf_points_num > 1 and 0 not in inds:
                ind1 = inds[:ind_inf_points[1] + 1]
                ind1 = np.append(ind1, ind1[-1] + 1)
                ind2 = inds[ind_inf_points[1] + 1:]
                ind2 = np.insert(ind2, 0, ind2[0] - 1)
                inds = [ind1, ind2]

            indices.append(inds)
        return np.array(indices)
