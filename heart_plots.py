from Classes.curve import Curve
from Classes.heart import Heart


# %% Defining Hearts for plotting
smooth_heart = Heart(12, 300)
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
    fig_size,
    filename=plot_directory +
    filename_smooth)

filename_edgy = f'one_colorful_edgy_heart.png'
edgy_heart.plot_colorful_heart(
    colors,
    fig_size,
    filename=plot_directory +
    filename_edgy)


# %% plotting hearts - one colorfull

filename_smooth = f'one_shaded_smooth_heart.png'
smooth_heart.plot_shaded_heart(
    colors[0],
    fig_size,
    filename=plot_directory +
    filename_smooth)

filename_edgy = f'one_shaded_edgy_heart.png'
edgy_heart.plot_shaded_heart(
    colors[0],
    fig_size,
    filename=plot_directory +
    filename_edgy)
