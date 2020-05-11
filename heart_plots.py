from Classes.curve import Curve
from Classes.heart import Heart
import matplotlib.pyplot as plt
import seaborn as sns
import random
from functions import *

# %% Defining Hearts for plotting
smooth_heart = Heart(12, 500)
edgy_heart = Heart(12, 2)

# %% Plotting parameters
plot_directory = 'HeartPlots/'
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

fig_size = (10, 10)

# %% plotting hearts - one colorfull

filename_smooth = f'one_colorful_smooth_heart.png'
fig_sm_c = smooth_heart.plot_colorful_heart(
    colors,
    fig_size)  # ,
# filename=plot_directory +
# filename_smooth)

filename_edgy = f'one_colorful_edgy_heart.png'
fig_ed_c = edgy_heart.plot_colorful_heart(
    colors,
    fig_size)  # ,
# filename=plot_directory +
# filename_edgy)


# %% plotting hearts - one shaded

facecolor = colors[0]
filename_smooth = f'one_shaded_smooth_heart_{facecolor}.png'
fig_sm_sh = smooth_heart.plot_shaded_heart(fig_size, facecolor)  # ,
# filename=plot_directory +
# filename_smooth)

filename_edgy = f'one_shaded_edgy_heart_{facecolor}.png'
fig_ed_sh = edgy_heart.plot_shaded_heart(fig_size, facecolor)  # ,
# filename=plot_directory +
# filename_edgy)


# %% some configurations - four hearts
filename = f'four_heart_plot_{facecolor}'
fig, axs = plt.subplots(2, 2)
fig.set_size_inches(30, 30)

for pol in fig_sm_c.patches:
    axs[0, 0].fill(pol.xy[:, 0], pol.xy[:, 1],
                   c=pol._facecolor[0:-1], edgecolor=pol._edgecolor)

axs[0, 0]._frameon = fig_sm_c._frameon
axs[0, 0].axis('off')

# =============================================================================
for pol in fig_sm_sh.patches:
    axs[1, 0].fill(pol.xy[:, 0], pol.xy[:, 1],
                   facecolor=pol._facecolor[0:-1], alpha=pol._alpha, edgecolor=None)

axs[1, 0]._frameon = fig_sm_sh._frameon
axs[1, 0].axis('off')

# =============================================================================
for pol in fig_ed_c.patches:
    axs[0, 1].fill(pol.xy[:, 0], pol.xy[:, 1],
                   c=pol._facecolor[0:-1], edgecolor=pol._edgecolor)

axs[0, 1]._frameon = fig_ed_c._frameon
axs[0, 1].axis('off')

# =============================================================================
for pol in fig_ed_sh.patches:
    axs[1, 1].fill(pol.xy[:, 0], pol.xy[:, 1],
                   facecolor=pol._facecolor[0:-1], alpha=pol._alpha, edgecolor=None)

axs[1, 1]._frameon = fig_ed_sh._frameon
axs[1, 1].axis('off')

plt.savefig(plot_directory + filename)

# %% some configurations - twelfe horizontals hearts
# filename_smooth = f'one_horiz_smooth_heart.png'


fig_sm_hor = []
for ind in range(len(colors)):
    fig_sm_hor.append(
        smooth_heart.plot_horizontal_heart(
            colors[ind], fig_size))

# %%
filename = f'twelve_heart_plot_horiz.png'
fig, axs = plt.subplots(4, 3)
fig.set_size_inches(30, 30)
fig_facecolor = [200 / 255, 200 / 255, 200 / 255]
fig.set_facecolor(fig_facecolor)

for ind in range(axs.size):
    f = fig_sm_hor[ind]
    for pol in f.patches:
        row = ind // 3
        col = ind - 3 * (ind // 3)
        axs[row, col].fill(pol.xy[:, 0], pol.xy[:, 1],
                           facecolor=pol._facecolor[0:-1],
                           alpha=pol._alpha,
                           edgecolor=None)
        axs[row, col].axis('equal')
        axs[row, col].axis('off')
plt.savefig(plot_directory + filename, facecolor=fig_facecolor)
plt.show()

# %%
filename = f'twelve_regular_heart_plot.png'
fig, axs = plt.subplots(4, 3)
fig.set_size_inches(30, 30)
fig_facecolor = [200 / 255, 200 / 255, 200 / 255]
fig.set_facecolor(fig_facecolor)

x = smooth_heart.x
y = smooth_heart.y

for ind in range(len(colors)):
    row = ind // 3
    col = ind - 3 * (ind // 3)

    axs[row, col].fill(x, y, facecolor=colors[ind], edgecolor=None)
    axs[row, col].axis('equal')
    axs[row, col].axis('off')

plt.savefig(plot_directory + filename, facecolor=fig_facecolor)
plt.show()

# %%
filename = f'twelve_border_heart_plot.png'
fig, axs = plt.subplots(4, 3)
fig.set_size_inches(30, 30)
fig_facecolor = [200 / 255, 200 / 255, 200 / 255]
fig.set_facecolor(fig_facecolor)

x = smooth_heart.x
y = smooth_heart.y

for ind in range(len(colors)):
    row = ind // 3
    col = ind - 3 * (ind // 3)

    axs[row, col].fill(x, y, facecolor=colors[ind], edgecolor=None, alpha=0.5)
    axs[row, col].plot(x, y, c=colors[ind], lw=5)
    axs[row, col].axis('equal')
    axs[row, col].axis('off')

plt.savefig(plot_directory + filename, facecolor=fig_facecolor)
plt.show()

# %%
color = colors[2]
filename = f'twelve_{color}_heart_plot_horiz.png'
fig, axs = plt.subplots(4, 3)
fig.set_size_inches(30, 30)
fig_facecolor = [10 / 255, 10 / 255, 10 / 255]
fig.set_facecolor(fig_facecolor)
for ind in range(axs.size):
    f = fig_sm_hor[ind]
    for pol in f.patches:
        row = ind // 3
        col = ind - 3 * (ind // 3)
        axs[row, col].fill(pol.xy[:, 0], pol.xy[:, 1],
                           facecolor=color,
                           alpha=(ind + 1) / axs.size,
                           edgecolor=None)
        axs[row, col].axis('equal')
        axs[row, col].axis('off')
plt.savefig(plot_directory + filename, facecolor=fig_facecolor)
plt.show()

# %%
fig, axs = plt.subplots(3, 4)
fig.set_size_inches(30, 30)

for ind in range(axs.size):
    f = fig_sm_hor[ind]
    for pol in f.patches:
        row = ind - 3 * (ind // 3)
        col = ind // 3
        axs[row, col].fill(pol.xy[:, 0], pol.xy[:, 1],
                           facecolor=pol._facecolor[0:-1],
                           alpha=pol._alpha,
                           edgecolor=None)
        axs[row, col].axis('equal')
        axs[row, col].axis('off')
