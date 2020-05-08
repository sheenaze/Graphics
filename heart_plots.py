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

fig_size = (20, 20)

# %% plotting hearts - one colorfull

filename_smooth = f'one_colorful_smooth_heart.png'
smooth_heart.plot_colorful_heart(
    colors,
    fig_size)  # ,
# filename=plot_directory +
# filename_smooth)

filename_edgy = f'one_colorful_edgy_heart.png'
edgy_heart.plot_colorful_heart(
    colors,
    fig_size)  # ,
# filename=plot_directory +
# filename_edgy)


# %% plotting hearts - one shaded

filename_smooth = f'one_shaded_smooth_heart.png'
smooth_heart.plot_shaded_heart(
    colors[0],
    fig_size)  # ,
# filename=plot_directory +
# filename_smooth)

filename_edgy = f'one_shaded_edgy_heart.png'
edgy_heart.plot_shaded_heart(
    colors[0],
    fig_size)  # ,
# filename=plot_directory +
# filename_edgy)

# %%
filename_smooth = f'one_horiz_smooth_heart.png'
for color in colors:
    smooth_heart.plot_horizontal_heart(color, fig_size)


# %% some configurations

fig = plt.figure(figsize=fig_size, frameon=True)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.plot(smooth_heart.x, smooth_heart.y, color='yellowgreen', lw=10)
plt.fill(smooth_heart.x, smooth_heart.y, c='yellowgreen', aa=True, alpha=0.3)
plt.show()
# plt.fill(smooth_heart.x, smooth_heart.y, c = 'purple', aa=True, hatch='O', fill=False)
