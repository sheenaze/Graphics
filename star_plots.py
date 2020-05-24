import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib
from Classes.other_shapes import *
import matplotlib.patches as pt

plot_directory = 'StarPlots/'

#%% colorful stars
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'}, frameon=False)
fig.set_size_inches(20, 20)

filename = 'colorful_stars.png'

NUM = 250

for i in range(NUM):
    center = np.random.rand(2) * 20

    arms_num = np.random.randint(5, 12)
    radius = np.random.rand()*0.5
    arm_length = radius + 0.1
    star = RegularStar(center, arms_num, radius, arm_length)

    vertices = star.get_vertices()
    facecolor = np.random.rand(3)
    alpha = np.random.rand()

    patch = pt.Polygon(vertices, facecolor=facecolor, edgecolor=None, alpha=alpha)
    ax.add_patch(patch)



ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.axis('off')
plt.savefig(plot_directory+filename)

#%% colorful stars
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'}, frameon=False, figsize=(10,10))
# fig.set_size_inches(10, 10)
fig_facecolor = 'midnightblue'

filename = 'night_sky.png'

NUM = 300

for i in range(NUM):
    center = np.random.rand(2) * 20

    arms_num = np.random.randint(5, 12)
    radius = np.random.rand()*0.25
    arm_length = radius + 0.1
    star = RegularStar(center, arms_num, radius, arm_length)

    vertices = star.get_vertices()
    facecolor = 'gold'
    alpha = np.random.rand()

    patch = pt.Polygon(vertices, facecolor=facecolor, edgecolor=None, alpha=alpha)
    ax.add_patch(patch)


ax.set_facecolor('midnightblue')
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.savefig(plot_directory+filename)
