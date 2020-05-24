import matplotlib.patches as pt
import matplotlib.pyplot as plt
from Classes.other_shapes import *
import matplotlib.path as mpath
Path = mpath.Path
"""
I am using matplotlib.patches library here, more info can be found on the website: https://matplotlib.org/api/patches_api.html
"""


class Face:
    def __init__(self, radius, facecolor='yellow',
                 edgecolor='black', linewidth=2, alpha=1, hatch=None):

        self.radius = radius
        self.facecolor = facecolor
        self.edgecolor = edgecolor
        self.lw = linewidth
        self.alpha = alpha
        self.hatch = hatch
# %% Face elements:

    def get_head(self, x, y):
        """

        Parameters
        ----------
        x : Float
            x coordinate of the head's center.
        y : Float
            y coordinate of the head's center.

        Returns
        -------
        head : matplotlib.patch Circle object


        """
        head = pt.Circle([x, y], self.radius,
                         facecolor=self.facecolor,
                         edgecolor=self.edgecolor,
                         lw=self.lw,
                         alpha=self.alpha,
                         hatch=self.hatch)
        return head

    def get_round_eye(self, x, y, radius, facecolor, edgecolor, hatch):
        """

        Parameters
        ----------
        x : Float
            x coordinate of the eye's center.
        y : Float
            y coordinate of the eye's center.
        radius : Float
            radius of an eye
        facecolor : None or color
            facecolor of an eye
        edgecolor : None or color
            edgececolor of an eye

        Returns
        -------
        eye : matplotlib.patch Circle object

        """

        eye = pt.Circle([x, y], radius=radius,
                        facecolor=facecolor, edgecolor=edgecolor, hatch=hatch)
        return eye

    def get_eye_pupil(self, x, y, radius, edgecolor, hatch):
        pupil = pt.Circle([x,
                           y],
                          radius=radius,
                          facecolor=facecolor,
                          edgecolor=edgecolor,
                          hatch=hatch)
        return pupil

    def get_star_eye(self, x, y, radius, num_arms,
                     facecolor, edgecolor, hatch, rotation):
        """

        Parameters
        ----------
        x : Float
            x coordinate of the eye's center.
        y : Float
            y coordinate of the eye's center.
        radius : Float
            radius of an eye
        num_arms : Integer
            number of arms of a star-eye
        facecolor : None or color
            facecolor of an eye
        edgecolor : None or color
            edgececolor of an eye

        Returns
        -------
        eye : matplotlib.patch Circle object

        """

        arm_height = radius * (1 + 0.2)
        star = RegularStar((x, y), num_arms, radius, arm_height, rotation)
        eye = pt.Polygon(star.get_vertices(), facecolor=facecolor,
                         edgecolor=edgecolor, hatch=hatch)
        return eye

    def get_arc_mouth(self, x, y, width, height, linewidth, facecolor,
                      hatch, edgecolor, angle=0.0, theta1=0, theta2=360):
        """


        Parameters
        ----------
        x : Float
            x coordinate of the mouth's center.
        y : Float
            y coordinate of the mouth's center.
        width : Float
            The length of the horizontal (x) axis.
        height : Float
            The length of the vertical (y) axis.
        linewidth : Float
            Width of the mouth line.
        facecolor : None or color
            Facecolor of the mouth line.
        edgecolor : None or color
            Edgecolor of the mouth line.
        angle : Float, optional
            Rotation of the ellipse in degrees (counterclockwise). The default is 0.0.
        theta1 : Float, optional
            Starting  angle of the arc in degrees. The default is 0.
        theta2 : Float, optional
            Ending angle of the arc in degrees.. The default is 360.

        Returns
        -------
        mouth : matplotlib.patch Arc object

        """

        mouth = pt.Arc([x, y], width, height, angle=angle,
                       theta1=theta1, theta2=theta2, lw=linewidth,
                       facecolor=facecolor, edgecolor=edgecolor, hatch=hatch)

        return mouth

    def get_laughing_mouth(self, x_center, y_center,
                           radius, linewidth, facecolor,
                           edgecolor, hatch):
        x0 = x_center - radius
        y0 = y_center
        xmax = x_center + radius
        ymin = y_center - radius * 2
        path = [
            (Path.MOVETO, [x0, y0]),
            (Path.CURVE4, [x_center, ymin]),
            (Path.CURVE4, [xmax, y0]),
            (Path.CURVE4, [xmax, y0]),
            (Path.CURVE4, [x_center, ymin * 0.4]),
            (Path.CURVE4, [x0, y0]),
            (Path.CURVE4, [x0, y0]),
            (Path.CLOSEPOLY, [x0, y0])]
        codes, verts = zip(*path)
        path = mpath.Path(verts, codes)

        mouth = pt.PathPatch(path, linewidth=linewidth, facecolor=facecolor,
                             edgecolor=edgecolor, hatch=hatch, alpha=0.9)

        return mouth

# %% Custom face

    def custom_face(self, eye_type, mouth_type, x=0, y=0,
                    eye_facecolor='black',
                    eye_edge_color=None,
                    eye_hatch=None,
                    mouth_facecolor='black',
                    mouth_edgecolor=None,
                    mouth_hatch=None):

        head = self.get_head(x, y)

        if eye_type == 'round':
            eye_x = self.radius * 0.35
            eye_y = self.radius * 0.35
            eye_radius = self.radius * 0.17
            left_eye = self.get_round_eye(-eye_x,
                                          eye_y,
                                          eye_radius,
                                          eye_facecolor,
                                          eye_edge_color,
                                          eye_hatch)
            right_eye = self.get_round_eye(
                eye_x,
                eye_y,
                eye_radius,
                eye_facecolor,
                eye_edge_color,
                eye_hatch)
        elif eye_type == 'star':
            eye_x = self.radius * 0.52
            eye_y = self.radius * 0.45
            eye_radius = self.radius * 0.3
            left_eye = self.get_star_eye(-eye_x,
                                         eye_y,
                                         eye_radius,
                                         5,
                                         eye_facecolor,
                                         eye_edge_color,
                                         eye_hatch,
                                         15)
            right_eye = self.get_star_eye(
                eye_x, eye_y, eye_radius, 5, eye_facecolor, eye_edge_color, eye_hatch, -15)

        if mouth_type == 'smiling_arc':
            smile_x = x
            smile_y = y - self.radius * 0.4

            smile_width = self.radius * 1.2
            smile_height = self.radius * 0.7

            smile = self.get_arc_mouth(
                smile_x,
                smile_y,
                smile_width,
                smile_height,
                10,
                mouth_facecolor,
                mouth_hatch,
                mouth_edgecolor,
                theta1=190,
                theta2=350)

        elif mouth_type == 'sad_arc':
            smile_x = x
            smile_y = y - self.radius * 0.6
            smile_width = self.radius * 1.2
            smile_height = self.radius * 0.7
            smile = self.get_arc_mouth(
                smile_x,
                smile_y,
                smile_width,
                smile_height,
                10,
                mouth_facecolor,
                mouth_hatch,
                mouth_edgecolor,
                theta1=10,
                theta2=170)
        elif mouth_type == 'shocked':
            smile_x = x
            smile_y = y - self.radius * 0.5

            smile_width = self.radius * 0.5
            smile_height = self.radius * 0.5

            smile = self.get_arc_mouth(
                smile_x,
                smile_y,
                smile_width,
                smile_height,
                10,
                mouth_facecolor,
                mouth_hatch,
                mouth_edgecolor,
                theta1=0,
                theta2=360)
        elif mouth_type == 'laughing':
            smile_x = x
            smile_y = y - self.radius * 0.15

            radius = self.radius * 0.8
            smile = self.get_laughing_mouth(
                smile_x,
                smile_y,
                radius,
                15,
                mouth_facecolor,
                mouth_edgecolor,
                mouth_hatch)

        return [head, left_eye, right_eye, smile]

# %% Defined face
    def smiling_face(
            self,
            x=0,
            y=0,
            eye_facecolor='black',
            eye_edge_color=None,
            eye_hatch=None,
            mouth_facecolor='black',
            mouth_edgecolor=None,
            mouth_hatch=None):
        """

        Parameters
        ----------
        x : Float, optional
            x coordinate of the head's center.. The default is 0.
        y : Float, optional
            y coordinate of the head's center.. The default is 0.
        eye_facecolor : None or color, optional
            Eyes facecolor. The default is 'black'.
        eye_edge_color : None or color, optional
             Eyes edgeecolor. The default is None.
        eye_hatch : None or pattern e.g.: 'o', '+', '*', optional
             the hatching pattern for eyes. The default is None.
        mouth_facecolor : None or color, optional
            Mouth facecolor. The default is 'black'.
        mouth_edgecolor : None or color, optional
            Mouth edgecolor. The default is None.
        mouth_hatch : None or pattern e.g.: 'o', '+', '*', optional
             the hatching pattern. The default is None.

        Returns
        -------
        list of matplotlib.patches objects

        """
        head = self.get_head(x, y)

        eye_x = self.radius * 0.35
        eye_y = self.radius * 0.35
        eye_radius = self.radius * 0.2

        left_eye = self.get_round_eye(-eye_x, eye_y, eye_radius,
                                      eye_facecolor, eye_edge_color, eye_hatch)
        right_eye = self.get_round_eye(
            eye_x,
            eye_y,
            eye_radius,
            eye_facecolor,
            eye_edge_color,
            eye_hatch)

        smile_x = x
        smile_y = y - self.radius * 0.4

        smile_width = self.radius * 1.2
        smile_height = self.radius * 0.7

        smile = self.get_arc_mouth(
            smile_x,
            smile_y,
            smile_width,
            smile_height,
            10,
            mouth_facecolor,
            mouth_hatch,
            mouth_edgecolor,
            theta1=190,
            theta2=350)

        return [head, left_eye, right_eye, smile]

    def sad_face(self, x=0, y=0, eye_facecolor='black',
                 eye_edge_color=None, eye_hatch=None, mouth_facecolor='black',
                 mouth_edgecolor=None, mouth_hatch=None):
        """

        Parameters
        ----------
        x : Float, optional
            x coordinate of the head's center.. The default is 0.
        y : Float, optional
            y coordinate of the head's center.. The default is 0.
        eye_facecolor : None or color, optional
            Eyes facecolor. The default is 'black'.
        eye_edge_color : None or color, optional
             Eyes edgeecolor. The default is None.
        eye_hatch : None or pattern e.g.: 'o', '+', '*', optional
             the hatching pattern for eyes. The default is None.
        mouth_facecolor : None or color, optional
            Mouth facecolor. The default is 'black'.
        mouth_edgecolor : None or color, optional
            Mouth edgecolor. The default is None.
        mouth_hatch : None or pattern e.g.: 'o', '+', '*', optional
             the hatching pattern. The default is None.

        Returns
        -------
        list of matplotlib.patches objects

        """
        head = self.get_head(x, y)

        eye_x = self.radius * 0.35
        eye_y = self.radius * 0.35
        eye_radius = self.radius * 0.2

        left_eye = self.get_round_eye(-eye_x, eye_y, eye_radius,
                                      eye_facecolor, eye_edge_color, eye_hatch)
        right_eye = self.get_round_eye(
            eye_x,
            eye_y,
            eye_radius,
            eye_facecolor,
            eye_edge_color,
            eye_hatch)

        smile_x = x
        smile_y = y - self.radius * 0.6

        smile_width = self.radius * 1.2
        smile_height = self.radius * 0.7

        smile = self.get_arc_mouth(
            smile_x,
            smile_y,
            smile_width,
            smile_height,
            10,
            mouth_facecolor,
            mouth_hatch,
            mouth_edgecolor,
            theta1=10,
            theta2=170)

        return [head, left_eye, right_eye, smile]

    def shocked_face(
            self,
            x=0,
            y=0,
            eye_facecolor='black',
            eye_edge_color=None,
            eye_hatch=None,
            mouth_facecolor='black',
            mouth_edgecolor=None,
            mouth_hatch=None):
        """

        Parameters
        ----------
        x : Float, optional
            x coordinate of the head's center.. The default is 0.
        y : Float, optional
            y coordinate of the head's center.. The default is 0.
        eye_facecolor : None or color, optional
            Eyes facecolor. The default is 'black'.
        eye_edge_color : None or color, optional
             Eyes edgeecolor. The default is None.
        eye_hatch : None or pattern e.g.: 'o', '+', '*', optional
             the hatching pattern for eyes. The default is None.
        mouth_facecolor : None or color, optional
            Mouth facecolor. The default is 'black'.
        mouth_edgecolor : None or color, optional
            Mouth edgecolor. The default is None.
        mouth_hatch : None or pattern e.g.: 'o', '+', '*', optional
             the hatching pattern. The default is None.

        Returns
        -------
        list of matplotlib.patches objects

        """
        head = self.get_head(x, y)

        eye_x = self.radius * 0.35
        eye_y = self.radius * 0.35
        eye_radius = self.radius * 0.2

        left_eye = self.get_round_eye(-eye_x, eye_y, eye_radius,
                                      eye_facecolor, eye_edge_color, eye_hatch)
        right_eye = self.get_round_eye(
            eye_x,
            eye_y,
            eye_radius,
            eye_facecolor,
            eye_edge_color,
            eye_hatch)

        smile_x = x
        smile_y = y - self.radius * 0.5

        smile_width = self.radius * 0.5
        smile_height = self.radius * 0.5

        smile = self.get_arc_mouth(
            smile_x,
            smile_y,
            smile_width,
            smile_height,
            10,
            mouth_facecolor,
            mouth_hatch,
            mouth_edgecolor,
            theta1=0,
            theta2=360)

        return [head, left_eye, right_eye, smile]

# %%


class CatFace(Face):
    pass
