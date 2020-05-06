import numpy as np
import math as mt
import matplotlib.pyplot as plt
from Classes.curve import Curve


class Heart(Curve):
    def __init__(self, number_of_pieces, number_of_points_per_piece):
        self.number_of_pieces = number_of_pieces
        self.number_of_points_per_piece = number_of_points_per_piece
        self.length = number_of_pieces * number_of_points_per_piece

        self.arg = np.linspace(0, 2 * mt.pi, self.length)
        self.x = 16 * np.sin(self.arg)**3
        self.y = 13 * np.cos(self.arg) - 5 * np.cos(2 * self.arg) - \
            2 * np.cos(3 * self.arg) - np.cos(4 * self.arg)

    def new_arg(self, new_length):
        return np.linspace(0, 2 * mt.pi, new_length)


    def new_x(self, new_length):
        new_arg = self.new_arg(new_length)
        return 16 * np.sin(new_arg)**3


    def new_y(self, new_length):
        new_arg = self.new_arg(new_length)
        return 13 * np.cos(new_arg) - 5 * np.cos(2 * new_arg) - \
            2 * np.cos(3 * new_arg) - np.cos(4 * new_arg)


    def plot_colorful_heart(self, colors, figsize, filename=None, frameon=True):
        """

        Parameters
        ----------
        colors : list
            list of colors, the length of the list should be the same as
            the number of pieces
        figsize : tuple
            tuple with size of the figure, eg. (20, 20)
        filename : string, optional
            name of the file for picture to be saved, if not defined file
            won't be saved
        frameon : bool, optional
            if False - transparent  The default is True.

        Returns
        -------
        plot of the heart

        """
        x = self.x
        y = self.y
        indices = self.get_nominal_ends()

        fig = plt.figure(figsize=figsize, frameon=frameon)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        for i in range(indices.size - 1):
            ind_1 = indices[i]
            ind_2 = indices[i + 1] + 1
            x_p = np.append(x[ind_1:ind_2], 0)
            y_p = np.append(y[ind_1:ind_2], 0)
            plt.fill(x_p, y_p, c=colors[i])

        if filename is not None:
            plt.savefig(filename)
        plt.show()


    def plot_shaded_heart(self, color, figsize, filename=None, frameon=True):
        """

        Parameters
        ----------
        color : string
            the main color of the heart
        figsize : tuple
            tuple with size of the figure, eg. (20, 20)
        filename : string, optional
            name of the file for picture to be saved, if not defined file
            won't be saved
        frameon : bool, optional
            if False - transparent  The default is True.

        Returns
        -------
        plot of the heart
        
        """
        x = self.x
        y = self.y
        indices = self.get_nominal_ends()
        
        fig = plt.figure(figsize=figsize)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        for i in range(indices.size - 1):
            ind_1 = indices[i]
            ind_2 = indices[i + 1]+1
            x_p = np.append(x[ind_1:ind_2], 0)
            y_p = np.append(y[ind_1:ind_2], 0)
            color = color
            plt.fill(x_p, y_p, c=color, alpha=(i + 1) / self.number_of_pieces)

        if filename is not None:
            plt.savefig(filename)
        plt.show()
