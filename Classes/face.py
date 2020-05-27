import math as mt
import matplotlib.patches as pt
from Classes.other_shapes import *
import matplotlib.path as mpath
import matplotlib.lines as mlines
Path = mpath.Path
"""
I am using matplotlib.patches library here, more info can be found
on the website: https://matplotlib.org/api/patches_api.html
"""


class Face:
    def __init__(self, radius, x=0, y=0,
                 facecolor='yellow',
                 edgecolor='black',
                 linewidth=2,
                 alpha=1,
                 hatch=None,
                 color=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.facecolor = facecolor
        self.edgecolor = edgecolor
        self.lw = linewidth
        self.alpha = alpha
        self.hatch = hatch
        self.color = color
# %% Face elements:

    def get_head(self):
        """

        Parameters
        ----------
        Returns
        -------
        head : matplotlib.patch Circle object


        """
        head = pt.Circle([self.x, self.y], self.radius,
                         facecolor=self.facecolor,
                         edgecolor=self.edgecolor,
                         lw=self.lw,
                         alpha=self.alpha,
                         hatch=self.hatch,
                         color=self.color)
        return head

    def get_eye(
            self,
            eye_type,
            side,
            x=None,
            y=None,
            radius=None,
            facecolor='black',
            edgecolor=None,
            hatch=None,
            color=None,
            rotation=None):
        """

        Parameters
        ----------
        eye_type : string
            'round', 'star'
        side : string
            'left' or 'right'
        x : Float or None (by default)
            x coordinate of an eye
        y : Float or None (by default)
            y coordinate of an eye
        radius : Float
            radius of an eye
        facecolor : None or color
            facecolor of an eye
        edgecolor : None or color
            edgececolor of an eye

        Returns
        -------
        eye : matplotlib.patch  object

        """
        if eye_type == 'round':
            if x is None and side == 'right':
                x = self.x + self.radius * 0.35
            elif x is None and side == 'left':
                x = self.x - self.radius * 0.35
            if y is None:
                y = self.y + self.radius * 0.35
            if radius is None:
                radius = self.radius * 0.17

            eye = pt.Circle([x, y],
                            radius=radius,
                            facecolor=facecolor,
                            edgecolor=edgecolor,
                            hatch=hatch,
                            color=color)

        elif eye_type == 'arc_up':
            if x is None and side == 'right':
                x = self.x + self.radius * 0.35
            elif x is None and side == 'left':
                x = self.x - self.radius * 0.35
            if y is None:
                y = self.y + self.radius * 0.35
            if radius is None:
                radius = self.radius * 0.17

            eye = pt.Arc([x, y],
                         3 * radius,
                         1.5 * radius,
                         theta1=10,
                         theta2=170,
                         lw=30,
                         edgecolor=facecolor,
                         hatch=hatch,
                         color=color)

        elif eye_type == 'arc_down':
            if x is None and side == 'right':
                x = self.x + self.radius * 0.35
            elif x is None and side == 'left':
                x = self.x - self.radius * 0.35
            if y is None:
                y = self.y + self.radius * 0.45
            if radius is None:
                radius = self.radius * 0.17

            eye = pt.Arc([x, y],
                         3 * radius,
                         1.5 * radius,
                         theta1=190,
                         theta2=350,
                         lw=30,
                         edgecolor=facecolor,
                         hatch=hatch,
                         color=color)

        elif eye_type == 'star':
            if rotation is None and side == 'right':
                rotation = -15
            elif rotation is None and side == 'left':
                rotation = 15

            if x is None and side == 'right':
                x = self.x + self.radius * 0.52
            elif x is None and side == 'left':
                x = self.x - self.radius * 0.52

            if y is None:
                y = self.y + self.radius * 0.45
            if radius is None:
                radius = self.radius * 0.3

            arm_height = radius * (1 + 0.2)

            star = RegularStar((x, y), 5, radius, arm_height, rotation)
            eye = star.get_as_patch(facecolor=facecolor, edgecolor=edgecolor,
                                    hatch=hatch, color=color)
        elif eye_type == 'heart':
            if rotation is None and side == 'right':
                rotation = -15
            elif rotation is None and side == 'left':
                rotation = 15

            if x is None and side == 'right':
                x = self.x + self.radius * 0.52
            elif x is None and side == 'left':
                x = self.x - self.radius * 0.52

            if y is None:
                y = self.y + self.radius * 0.45
            if radius is None:
                radius = self.radius * 0.5

            heart = HeartPatch(x, y, radius, facecolor,
                               edgecolor, hatch, color)
            eye = heart.get_as_patch(rotation)

        return eye

    def get_pupil(self, pupil_type, eye_side, pupil_pos_vert, pupil_pos_hor,
                  x=None, y=None, radius=None, facecolor='white',
                  edgecolor=None, hatch=None, color=None):

        if pupil_type == 'round':
            eye_radius = self.radius * 0.17
            if radius is None:
                radius = self.radius * 0.085

            if x is None:
                if eye_side == 'right':
                    eye_x = self.x + self.radius * 0.35
                elif eye_side == 'left':
                    eye_x = self.x - self.radius * 0.35

                if pupil_pos_hor == 'center':
                    x = eye_x
                elif pupil_pos_hor == 'left':
                    if pupil_pos_vert == 'center':
                        x = eye_x - eye_radius + radius
                    else:
                        x = eye_x - mt.sqrt(2) / 2 * radius
                elif pupil_pos_hor == 'right':
                    if pupil_pos_vert == 'center':
                        x = eye_x + eye_radius - radius
                    else:
                        x = eye_x + mt.sqrt(2) / 2 * radius

            if y is None:

                eye_y = self.y + self.radius * 0.35

                if pupil_pos_vert == 'center':
                    y = eye_y

                elif pupil_pos_vert == 'up':
                    if pupil_pos_vert == 'center':
                        y = eye_y + eye_radius - radius
                    else:
                        y = eye_y + mt.sqrt(2) / 2 * radius

                elif pupil_pos_vert == 'down':
                    if pupil_pos_vert == 'center':
                        y = eye_y - eye_radius + radius
                    else:
                        y = eye_y - mt.sqrt(2) / 2 * radius

            pupil = pt.Circle([x, y], radius, facecolor=facecolor,
                              edgecolor=edgecolor, hatch=hatch, color=color)

        elif pupil_type is None:
            pupil = pt.Circle([0, 0], radius=0)

        return pupil

    def get_mouth(self, mouth_type, width=None, height=None,
                  linewidth=10, facecolor='pink', hatch=None, edgecolor=None,
                  angle=0.0, theta1=0, theta2=360, color=None):
        """

        Parameters
        ----------
        mouth_type : string
            'smiling_arc', 'sad_arc', 'shocked', laughing
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
        mouth : matplotlib.patch object

        """
        if mouth_type == 'smiling_arc':

            x = self.x
            y = self.y - self.radius * 0.4

            if width is None:
                width = self.radius * 1.2

            if height is None:
                height = self.radius * 0.7

            mouth = pt.Arc([x, y], width, height, angle=angle,
                           theta1=190, theta2=350, lw=linewidth,
                           facecolor=facecolor, edgecolor=edgecolor, hatch=hatch)

        elif mouth_type == 'sad_arc':
            x = self.x
            y = self.y - self.radius * 0.6

            if width is None:
                width = self.radius * 1.2

            if height is None:
                height = self.radius * 0.7

            mouth = pt.Arc([x, y], width, height, angle=angle,
                           theta1=10, theta2=170, lw=linewidth,
                           facecolor=facecolor, edgecolor=edgecolor, hatch=hatch)

        elif mouth_type == 'shocked':
            x = self.x
            y = self.y - self.radius * 0.5

            if width is None:
                width = self.radius * 0.5
            if height is None:
                height = self.radius * 0.5

            mouth = pt.Arc([x, y], width, height, angle=angle,
                           theta1=0, theta2=360, lw=linewidth,
                           facecolor=facecolor, edgecolor=edgecolor, hatch=hatch)
        elif mouth_type is None:
            mouth = pt.Circle([0, 0], radius=0)

        elif mouth_type == 'laughing':
            x_center = self.x
            y_center = self.y - self.radius * 0.15
            radius = self.radius * 0.8

            x0 = x_center - radius
            y0 = y_center
            xmax = x_center + radius
            ymin = y_center - radius * 2
            path = [(Path.MOVETO, [x0, y0]),
                    (Path.CURVE4, [x_center, ymin]),
                    (Path.CURVE4, [xmax, y0]),
                    (Path.CURVE4, [xmax, y0]),
                    (Path.CURVE4, [x_center, ymin * 0.4]),
                    (Path.CURVE4, [x0, y0]),
                    (Path.CURVE4, [x0, y0]),
                    (Path.CLOSEPOLY, [x0, y0])]
            codes, verts = zip(*path)
            path = mpath.Path(verts, codes)

            mouth = pt.PathPatch(path, linewidth=linewidth,
                                 facecolor=facecolor,
                                 color=color,
                                 edgecolor=edgecolor,
                                 hatch=hatch, alpha=0.9)
        return mouth

    def get_ear(
            self,
            shape,
            side,
            x=None,
            y=None,
            rotation=0,
            width=0,
            height=0,
            linewidth=30,
            color='black'):

        if x is None and side == 'left':
            x = self.x - self.radius * 0.5
        elif x is None and side == 'right':
            x = self.x + self.radius * 0.5
        if y is None:
            y = self.y + self.radius * 0.65

        if shape == 'pointy':
            xs = [x, x - width / 2, x, x + width / 2]
            ys = [y, y, y + height, y]
            XY = rotation_in_place(np.array([xs, ys]).T, rotation)

            ear = mlines.Line2D(XY[1:, 0], XY[1:, 1], linewidth,
                                color=color, solid_capstyle='round')
        elif shape is None:
            ear = mlines.Line2D([0, 0], [0, 0], linewidth=0)
        return ear

    def get_nose(self, shape, radius, x=None, y=None, facecolor='black',
                 rotation=0, edgecolor=None, color=None, hatch=None):

        if x is None:
            x = self.x
        if y is None:
            y = self.y

        if shape == 'star':
            star = RegularStar([[x, y]], 5, radius, radius * 1.2, rotation)
            nose = star.get_as_patch(facecolor, edgecolor, hatch, color)
        elif shape == 'round':
            nose = pt.Circle([x, y], radius, facecolor=facecolor,
                             edgecolor=edgecolor, hatch=hatch, color=color)
        elif shape == 'heart':
            heart = HeartPatch(x, y, radius, facecolor, edgecolor, hatch)
            nose = heart.get_as_patch(rotation)
        elif shape is None:
            nose = pt.Circle([0, 0], radius=0)

        return nose
# %% Custom face

    def custom_face(
            self,
            eye_type,
            mouth_type,
            nose_shape=None,
            ear_shape=None,
            pupil_type=None,
            x_eye=None,
            y_eye=None,
            eye_radius=None,
            eye_facecolor='black',
            eye_edgecolor=None,
            eye_hatch=None,
            mouth_width=None,
            mouth_height=None,
            mouth_linewidth=10,
            mouth_facecolor=None,
            mouth_edgecolor=None,
            mouth_hatch=None,
            x_pupil=None,
            y_pupil=None,
            pupil_radius=0,
            pupil_vert_pos='center',
            pupil_hor_pos='center',
            pupil_facecolor=None,
            pupil_edgecolor=None,
            pupil_hatch=None,
            x_nose=None,
            y_nose=None,
            nose_radius=0,
            nose_rotation=0,
            nose_facecolor=None,
            nose_edgecolor=None,
            nose_hatch=None,
            x_ear=None,
            y_ear=None,
            ear_color=None,
            ear_width=0,
            ear_height=0,
            ear_linewidth=30,
            ear_rotation=0):

        head = self.get_head()
        left_eye = self.get_eye(eye_type, 'left', x_eye, y_eye, eye_radius,
                                eye_facecolor, eye_edgecolor, eye_hatch)

        right_eye = self.get_eye(eye_type, 'right', x_eye, y_eye, eye_radius,
                                 eye_facecolor, eye_edgecolor, eye_hatch)
        nose = self.get_nose(nose_shape, nose_radius, x_nose, y_nose,
                             nose_facecolor, nose_rotation, nose_edgecolor,
                             nose_hatch)
        left_ear = self.get_ear(
            ear_shape,
            'left',
            x_ear,
            y_ear,
            ear_rotation,
            ear_width,
            ear_height,
            ear_linewidth,
            ear_color)

        right_ear = self.get_ear(
            ear_shape,
            'right',
            x_ear,
            y_ear,
            -ear_rotation,
            ear_width,
            ear_height,
            ear_linewidth,
            ear_color)

        mouth = self.get_mouth(
            mouth_type,
            mouth_width,
            mouth_height,
            mouth_linewidth,
            mouth_facecolor,
            mouth_hatch,
            mouth_edgecolor)

        left_pupil = self.get_pupil(
            pupil_type,
            'left',
            pupil_vert_pos,
            pupil_hor_pos,
            x_pupil,
            y_pupil,
            pupil_radius,
            pupil_facecolor,
            pupil_edgecolor,
            pupil_hatch)

        right_pupil = self.get_pupil(
            pupil_type,
            'right',
            pupil_vert_pos,
            pupil_hor_pos,
            x_pupil,
            y_pupil,
            pupil_radius,
            pupil_facecolor,
            pupil_edgecolor,
            pupil_hatch)

        return [head, left_eye, right_eye, mouth, right_pupil,
                left_pupil, nose, left_ear, right_ear]

# %% Defined face
    def smiling_face(
            self,
            eye_facecolor='black',
            eye_edge_color=None,
            eye_hatch=None,
            mouth_facecolor='black',
            mouth_edgecolor=None,
            mouth_hatch=None):
        """

        Parameters
        ----------
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
        head = self.get_head()

        left_eye = self.get_eye('round', 'left', None, None, None,
                                eye_facecolor, eye_edge_color, eye_hatch)
        right_eye = self.get_eye('round', 'right', None, None, None,
                                 eye_facecolor, eye_edge_color, eye_hatch)

        smile = self.get_mouth('smiling_arc')

        return [head, left_eye, right_eye, smile]

    def sad_face(self, eye_facecolor='black',
                 eye_edge_color=None, eye_hatch=None, mouth_facecolor='black',
                 mouth_edgecolor=None, mouth_hatch=None):
        """

        Parameters
        ----------
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
        head = self.get_head()

        left_eye = self.get_eye('round', 'left', None, None, None,
                                eye_facecolor, eye_edge_color, eye_hatch)
        right_eye = self.get_eye('round', 'right', None, None, None,
                                 eye_facecolor, eye_edge_color, eye_hatch)
        smile = self.get_mouth('sad_arc')

        return [head, left_eye, right_eye, smile]

    def shocked_face(
            self,
            eye_facecolor='black',
            eye_edge_color=None,
            eye_hatch=None,
            mouth_facecolor='black',
            mouth_edgecolor=None,
            mouth_hatch=None):
        """

        Parameters
        ----------
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
        head = self.get_head()

        left_eye = self.get_eye('round', 'left', None, None, None,
                                eye_facecolor, eye_edge_color, eye_hatch)
        right_eye = self.get_eye('round', 'right', None, None, None,
                                 eye_facecolor, eye_edge_color, eye_hatch)

        smile = self.get_mouth('shocked')

        return [head, left_eye, right_eye, smile]

# %%


class CatFace(Face):
    pass

    def __init__(self, radius, x=0, y=0, facecolor='yellow', edgecolor='black',
                 linewidth=2, alpha=1, hatch=None, color=None):
        super().__init__(radius, x, y, facecolor, edgecolor,
                         linewidth, alpha, hatch, color)

    def get_whiskers(
            self,
            side,
            length,
            width,
            color,
            number=3,
            start_angle=15):

        if side == 'left':
            x0 = self.x - self.radius * 0.5
            dfi = (180 - start_angle) / (number)
        elif side == 'right':
            x0 = self.x + self.radius * 0.5
            dfi = (-180 - start_angle) / (number)
        y0 = self.y + self.radius * 0.01 * number

        whiskers = []
        for ind in range(number):
            angle = start_angle + ind * dfi
            ends = np.array([[x0, x0], [y0, y0 + length]])
            right_ends = rotation_in_place(ends.T, angle)
            y0 -= self.radius * 0.02 * number

            whisker = mlines.Line2D(
                right_ends[:, 0], right_ends[:, 1], color=color,
                linewidth=width, solid_capstyle='round')
            whiskers.append(whisker)

        return whiskers

    def get_cat_face(
            self,
            eye_type,
            mouth_type,
            nose_shape,
            ear_shape='pointy',
            pupil_type=None,
            x_eye=None,
            y_eye=None,
            eye_radius=None,
            eye_facecolor='black',
            eye_edgecolor=None,
            eye_hatch=None,
            mouth_width=None,
            mouth_height=None,
            mouth_linewidth=10,
            mouth_facecolor=None,
            mouth_edgecolor=None,
            mouth_hatch=None,
            x_pupil=None,
            y_pupil=None,
            pupil_radius=0,
            pupil_vert_pos='center',
            pupil_hor_pos='center',
            pupil_facecolor=None,
            pupil_edgecolor=None,
            pupil_hatch=None,
            x_nose=None,
            y_nose=None,
            nose_radius=0,
            nose_rotation=0,
            nose_facecolor=None,
            nose_edgecolor=None,
            nose_hatch=None,
            x_ear=None,
            y_ear=None,
            ear_color=None,
            ear_width=0,
            ear_height=0,
            ear_linewidth=30,
            ear_rotation=0,
            whiskers_number=3,
            whiskers_length=0,
            whiskers_width=10,
            whiskers_color=None,
            whiskers_start_angle=45):

        face = self.custom_face(
            eye_type,
            mouth_type,
            nose_shape,
            ear_shape,
            pupil_type,
            x_eye,
            y_eye,
            eye_radius,
            eye_facecolor,
            eye_edgecolor,
            eye_hatch,
            mouth_width,
            mouth_height,
            mouth_linewidth,
            mouth_facecolor,
            mouth_edgecolor,
            mouth_hatch,
            x_pupil,
            y_pupil,
            pupil_radius,
            pupil_vert_pos,
            pupil_hor_pos,
            pupil_facecolor,
            pupil_edgecolor,
            pupil_hatch,
            x_nose,
            y_nose,
            nose_radius,
            nose_rotation,
            nose_facecolor,
            nose_edgecolor,
            nose_hatch,
            x_ear,
            y_ear,
            ear_color,
            ear_width,
            ear_height,
            ear_linewidth,
            ear_rotation)

        left_whiskers = self.get_whiskers(
            'left',
            whiskers_length,
            whiskers_width,
            whiskers_color,
            whiskers_number,
            whiskers_start_angle)

        right_whiskers = self.get_whiskers(
            'right',
            whiskers_length,
            whiskers_width,
            whiskers_color,
            whiskers_number,
            -whiskers_start_angle)

        for whisker_left, whisker_right in zip(left_whiskers, right_whiskers):
            face.append(whisker_left)
            face.append(whisker_right)

        return face
