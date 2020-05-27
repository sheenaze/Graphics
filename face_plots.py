from Classes.face import *
from Classes.my_plots import *
from Classes.my_plots import *
from Classes.other_shapes import *
import matplotlib.pyplot as plt


# %% some general settings
radius = 10
offset = 2
figsize = (20, 20)

xlim = [-(radius + offset), radius + offset]
ylim = [-(radius + offset), radius + offset]
plot_directory = 'FacePlots/'


# %% cat face plot
fig_facecolor = [0, 0, 0]
filename = f'cat_face.png'


cat_face = CatFace(radius, facecolor='black', edgecolor='black')
cat_face_to_plot = cat_face.get_cat_face(
    eye_type='round',
    mouth_type='smiling_arc',
    nose_shape='heart',
    ear_shape='pointy',
    pupil_type='round',
    x_eye=None,
    y_eye=None,
    eye_radius=None,
    eye_facecolor='white',
    eye_edgecolor=None,
    eye_hatch=None,
    mouth_width=None,
    mouth_height=None,
    mouth_linewidth=10,
    mouth_edgecolor=None,
    mouth_hatch=None,
    x_pupil=None,
    y_pupil=None,
    pupil_radius=None,
    pupil_vert_pos='down',
    pupil_hor_pos='left',
    pupil_facecolor='black',
    pupil_edgecolor=None,
    pupil_hatch=None,
    x_nose=cat_face.x,
    y_nose=cat_face.y,
    nose_radius=1,
    nose_rotation=0,
    nose_facecolor='pink',
    nose_edgecolor=None,
    nose_hatch=None,
    x_ear=None,
    y_ear=None,
    ear_color='white',
    ear_width=radius * 0.3,
    ear_height=radius * 0.4,
    ear_linewidth=20,
    ear_rotation=15,
    whiskers_number=3,
    whiskers_length=8,
    whiskers_width=10,
    whiskers_color='white',
    whiskers_start_angle=75)


faces_plot = MyPlots(figsize, fig_facecolor, (2, 2))
faces_plot.single_plot(cat_face_to_plot, 'black', [-15, 15], [-15, 15],
                       filename=plot_directory + filename)


# %% star-eye laughing face
face_color = 'yellow'
eye_color = 'blue'
mouth_color = 'white'
filename = f'arc_eye_face.png'
fig_facecolor = [1, 1, 1]

face = Face(radius, facecolor=face_color, linewidth=5)
face_to_print = face.custom_face(
    eye_type='arc_down',
    mouth_type='laughing',
    eye_facecolor='black',
    mouth_facecolor='white',
    mouth_edgecolor='black')
faces_plot = MyPlots(figsize, fig_facecolor, (2, 2))
faces_plot.single_plot(face_to_print, 'white', [-15, 15], [-15, 15],
                       filename=plot_directory + filename)



# %% star-eye laughing face
face_color = 'yellow'
eye_color = 'blue'
mouth_color = 'white'
filename = f'star_eye_laughing_face.png'


face = Face(radius, facecolor=face_color, linewidth=5)
face_to_print = face.custom_face(
    'star',
    'laughing',
    eye_facecolor='deepskyblue',
    eye_hatch='*',
    mouth_facecolor='white',
    mouth_edgecolor='black')
faces_plot = MyPlots(figsize, fig_facecolor, (2, 2))
faces_plot.single_plot(face_to_print, 'white', [-15, 15], [-15, 15],
                       filename=plot_directory + 'star_eyeface.png')

plt.savefig(plot_directory + filename)

# %% 2x2 laughing faces plots
face_color = ['#12e2a3', '#a3de83', '#c8d35b', '#e6739f']
edgecolor = ['#389168', '#38817a', '#6b3278', '#790c5a']
eye_color = ['#573697', '#346473', '#46265c', '#cc0e74']
eye_type = ['star', 'arc_up', 'arc_down', 'heart']
mouth_color = 'white'
eye_hatch = ['*', None, None, 'o']
filename = f'laughing_faces.png'
backg_colors = ['#ddf516',
                '#f7f39a',
                '#e0f6aa',
                '#ffb2a7']

faces_to_plot = []
for i in range(4):
    face = Face(
        radius,
        edgecolor=edgecolor[i],
        facecolor=face_color[i],
        linewidth=5)
    face_to_plot = face.custom_face(
        eye_type[i],
        'laughing',
        eye_facecolor=eye_color[i],
        eye_hatch=eye_hatch[i],
        mouth_facecolor='white',
        mouth_edgecolor=edgecolor[i])
    faces_to_plot.append(face_to_plot)

faces_plot = MyPlots(figsize, fig_facecolor, (2, 2))
faces_plot.plot_patches_pattern(faces_to_plot, backg_colors, xlim, ylim)
plt.savefig(plot_directory + filename)

# %% Pop-art 2x2 plot
pop_art_backg_colors = ['deeppink',
                        'deepskyblue',
                        'greenyellow',
                        'purple']
pop_art_face_colors = ['yellow',
                       'magenta',
                       'turquoise',
                       'lawngreen']
filename = f'pop_art_smiling_faces.png'
faces_to_plot = []
for i in range(4):
    face = Face(radius, facecolor=pop_art_face_colors[i], hatch='.o')
    faces_to_plot.append(face.smiling_face())

faces_plot = MyPlots(figsize, fig_facecolor, (2, 2))
faces_plot.plot_patches_pattern(
    faces_to_plot, pop_art_backg_colors, xlim, ylim, filename=plot_directory+filename)


# %% some other plots
colors = [
    'purple',
    'brown',
    'crimson',
    'chocolate',
    'orange',
    'gold',
    'yellowgreen',
    'green',
    'deepskyblue',
    'steelblue',
    'darkblue',
    'indigo']

smiling_faces = []
sad_faces = []
shocked_faces = []
for i in range(12):
    face = Face(radius, facecolor=colors[i], alpha=0.7)
    smiling_faces.append(face.smiling_face())
    sad_faces.append(face.sad_face())
    shocked_faces.append(face.shocked_face())


xlim = [-(radius + 5), radius + 5]
ylim = [-(radius + offset), radius + offset]
twelve_faces_plot = MyPlots(figsize, fig_facecolor, (4, 3))
twelve_faces_plot.plot_patches_pattern(smiling_faces, 'white', xlim, ylim)
twelve_faces_plot.plot_patches_pattern(sad_faces, 'white', xlim, ylim)
twelve_faces_plot.plot_patches_pattern(shocked_faces, 'white', xlim, ylim)
