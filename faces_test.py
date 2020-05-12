import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math as mt
from test_functions import *
from Classes.curve import * 
from Classes.face import *
import matplotlib.patches as pt

radius = 5
big_circle = pt.Circle([0, 0], radius = radius, facecolor='yellow', edgecolor='black', linewidth=4)
small_circle_left = pt.Circle([-radius*0.35, radius*0.35], radius=radius*0.2, facecolor='black')
small_circle_right = pt.Circle([radius*0.35, radius*0.35], radius=radius*0.2, facecolor='black')
smile = pt.Arc([0, -radius*0.4], radius*1.2, radius*.7, theta1=190, theta2=350, lw=10)
patch = pt.Patch(edgecolor='black', facecolor='blue')

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
fig.set_size_inches(20, 20)
ax.add_patch(big_circle)
ax.add_patch(small_circle_left)
ax.add_patch(small_circle_right)
ax.add_patch(smile)


ax.set_xlim(-(radius+1), radius + 1)
ax.set_ylim(-(radius+1), radius + 1)

plt.show()

face1 = Face(radius)
face2 = Face(radius, 'pink')

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
fig.set_size_inches(20, 20)
for element in face2.smiling_face():
    ax.add_patch(element)
    

ax.set_xlim(-(radius+1), radius + 1)
ax.set_ylim(-(radius+1), radius + 1)

plt.show()

#%%
NUM = 250

ells = [pt.Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]
ells1 = ells.copy()

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
fig.set_size_inches(20, 20)
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.show()
