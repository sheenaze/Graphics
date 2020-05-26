import numpy as np
import math as mt
import matplotlib.pyplot as plt
import matplotlib.patches as pt
from Classes.curve import Curve
from functions import *


class RegularStar:
    def __init__(self, center, num_arms, radius, arm_height, star_rotation=0):
        self.center = center
        self.num_arms = num_arms
        self.radius = radius
        self.arm_height = arm_height
        self.star_rotation = star_rotation

    def get_star_base(self):
        """
        stars are based on n-vertex regular polygons

        Returns
        -------
        numpy array
            an array of coordinates of vertices

        """
        base = pt.RegularPolygon((0, 0), self.num_arms, self.radius)
        base_vertices = base.get_verts()
        # sum_ang = 180 * (self.num_arms - 2)
        # internal_ang = sum_ang / self.num_arms
        fi = (360 / self.num_arms / 2 + self.star_rotation) * \
            mt.pi / 180  # (internal_ang) * mt.pi / 180
        return np.dot(rotation_matrix(fi), base_vertices.T).T + self.center

    def get_base_arm(self):
        """


        Returns
        -------
        3x2 numpy array
            coordinates of vertices of an isosceles triangle which is a base for an arm

        """
        a = self.radius * 2 * mt.sin(mt.pi / self.num_arms)
        return np.array([[self.center[0], self.center[1]],
                         [self.center[0] + a / 2, self.center[1] + self.arm_height],
                         [self.center[0] + a, self.center[1]]])

    def get_vertices(self):
        """

        Returns
        -------
        star_verts : Nx2 numpy array
            coordinates of vertices of a star

        """

        base_vertices = self.get_star_base()
        base_triangle_verts = self.get_base_arm()
        star_verts = np.empty((0, 2))

        for ind in range(len(base_vertices) - 1):
            base_dx = base_vertices[ind + 1, 0] - base_vertices[ind, 0]
            base_dy = base_vertices[ind + 1, 1] - base_vertices[ind, 1]
            fi = mt.atan2(base_dy, base_dx) + mt.pi
            rot_triangle_verts = np.dot(
                rotation_matrix(fi), base_triangle_verts.T).T
            shift_x = base_vertices[ind, 0] - rot_triangle_verts[-1, 0]
            shift_y = base_vertices[ind, 1] - rot_triangle_verts[-1, 1]
            arm_vertices = [base_vertices[ind, :], rot_triangle_verts[1, :] +
                            np.array([shift_x, shift_y]), base_vertices[ind + 1, :]]
            # arm_vertices = rot_triangle_verts + np.array([shift_x, shift_y])

            star_verts = np.append(star_verts, arm_vertices, axis=0)

        return star_verts

    def get_as_patch(self, facecolor=None,
                     edgecolor=None,
                     hatch=None,
                     color=None):
        vertices = self.get_vertices()
        patch = pt.Polygon(vertices, facecolor=facecolor,
                           edgecolor=edgecolor, hatch=hatch, color=color)
        return patch


class HeartPatch:
    def __init__(self, x, y, radius, facecolor='black',
                 edgecolor=None, hatch=None, color=None):

        self.arg = np.linspace(0, 2 * mt.pi, 1000)
        self.x = radius * np.sin(self.arg)**3
        self.y = (0.8125 * np.cos(self.arg) - 0.3125 * np.cos(2 * self.arg) -
                  0.125 * np.cos(3 * self.arg) - 0.0625 * np.cos(4 * self.arg)) * radius
        self.facecolor = facecolor
        self.edgecolor = edgecolor
        self.hatch = hatch
        self.color = color

    def get_as_patch(self, rotation=0, linewidth=0):
        XY = np.array([self.x, self.y])
        XY = rotation_in_place(XY.T, rotation)

        patch = pt.Polygon(XY,
                           facecolor=self.facecolor,
                           edgecolor=self.edgecolor,
                           hatch=self.hatch,
                           color=self.color,
                           linewidth=linewidth)
        return patch
