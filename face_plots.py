from Classes.face import *
import matplotlib.patches as pt
import matplotlib.pyplot as plt

# %%
radius = 10
plot_directory = 'FacePlots/'
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

# %%
filename = f'twelve_colorful_faces.png'
fig, axs = plt.subplots(4, 3)
fig.set_size_inches(30, 30)
fig_facecolor = [1, 1, 1]
fig.set_facecolor(fig_facecolor)

for ind in range(len(colors)):
    row = ind // 3
    col = ind - 3 * (ind // 3)

    face = Face(radius, colors[ind], alpha=0.7)
    for element in face.smiling_face():
        axs[row, col].add_patch(element)
        axs[row, col].set_xlim(-(radius + 1), radius + 1)
        axs[row, col].set_ylim(-(radius + 1), radius + 1)
        axs[row, col].axis('equal')
        axs[row, col].axis('off')

plt.savefig(plot_directory + filename, facecolor=fig_facecolor)
plt.show()
