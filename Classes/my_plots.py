import matplotlib.patches as pt
import matplotlib.pyplot as plt


class MyPlots:
    def __init__(self, figsize, fig_facecolor, axs_configuration=None,
                 frameon=True):

        self.figsize = figsize
        self.fig_facecolor = fig_facecolor
        self.axs_configuration = axs_configuration
        self.frameon = frameon

    def plot_patches_pattern(
                self,
                list_of_patches,
                background_colors,
                xlim,
                ylim,
                vspace=0,
                hspace=0,
                equal_axes=True,
                spines_off=True,
                filename=None):

        rows_num = self.axs_configuration[0]
        cols_num = self.axs_configuration[1]
        fig, axs = plt.subplots(rows_num, cols_num, frameon=self.frameon)
        fig.set_size_inches(self.figsize)
        fig.subplots_adjust(hspace=vspace, wspace=hspace)

        for ind in range(rows_num * cols_num):
            if rows_num >= cols_num:
                row = ind // cols_num
                col = ind - cols_num * (ind // cols_num)
            else:
                row = ind - cols_num * (ind // cols_num)
                col = ind // cols_num

            patches = list_of_patches[ind]

            if type(background_colors) == list:
                background_color = background_colors[ind]
            else:
                background_color = background_colors

            for element in patches:
                axs[row, col].add_patch(element)
                if equal_axes:
                    axs[row, col].axis('equal')

                axs[row, col].get_xaxis().set_visible(False)
                axs[row, col].set_xlim(xlim)
                axs[row, col].get_yaxis().set_visible(False)
                axs[row, col].set_ylim(ylim)
                axs[row, col].set_facecolor(background_color)

                if spines_off:
                    axs[row, col].spines['top'].set_visible(False)
                    axs[row, col].spines['right'].set_visible(False)
                    axs[row, col].spines['bottom'].set_visible(False)
                    axs[row, col].spines['left'].set_visible(False)
                        
        if filename is not None:
            plt.savefig(filename, facecolor=self.fig_facecolor)
