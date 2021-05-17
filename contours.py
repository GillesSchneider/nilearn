from nilearn.plotting.displays import *
from nilearn.plotting.img_plotting import *

from nilearn.datasets import *


motor_images = fetch_neurovault_motor_task()
stat_img = motor_images.images[0]

display = plot_glass_brain(None, colorbar=False, title='plot_stat_map')


cmap = 'YlOrRd'

levels=[[3, 6], [5, 7]]
display.add_contours(stat_img, show_level=False, filled=True, levels = levels, cmap=cmap)


show()