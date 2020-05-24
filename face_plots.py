from Classes.face import *
from Classes.my_plots import *
from Classes.my_plots import *
from Classes.other_shapes import *
import matplotlib.pyplot as plt

# %% some general settings
radius = 10
offset = 2
figsize = (20, 20)
fig_facecolor = [1, 1, 1]
xlim = [-(radius + offset), radius + offset]
ylim = [-(radius + offset), radius + offset]
plot_directory = 'FacePlots/'

# %% star-eye face
face_color = 'yellow'
eye_color = 'blue'
mouth_color = 'white'
filename = f'star_eye_laughing_face.png'

face = Face(radius, face_color, linewidth=5)
face_to_print = face.custom_face(
    'star',
    'laughing',
    eye_facecolor='deepskyblue',
    mouth_facecolor='white',
    mouth_edgecolor='black')
faces_plot = MyPlots(figsize, fig_facecolor, (2, 2))
faces_plot.single_plot(face_to_print, 'white', [-15, 15], [-15, 15],
                       filename=plot_directory + 'star_eyeface.png')

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
    face = Face(radius, pop_art_face_colors[i], hatch='.o')
    faces_to_plot.append(face.smiling_face())

faces_plot = MyPlots(figsize, fig_facecolor, (2, 2))
faces_plot.plot_patches_pattern(
    faces_to_plot, pop_art_backg_colors, xlim, ylim)


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
    face = Face(radius, colors[i], alpha=0.7)
    smiling_faces.append(face.smiling_face())
    sad_faces.append(face.sad_face())
    shocked_faces.append(face.shocked_face())

twelve_faces_plot = MyPlots(figsize, fig_facecolor, (4, 3))
twelve_faces_plot.plot_patches_pattern(smiling_faces, 'white', xlim, ylim)
twelve_faces_plot.plot_patches_pattern(sad_faces, 'white', xlim, ylim)
twelve_faces_plot.plot_patches_pattern(shocked_faces, 'white', xlim, ylim)
