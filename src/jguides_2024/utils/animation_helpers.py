import os

import matplotlib.animation as animation

from jguides_2024.utils.plot_helpers import get_default_plot_save_dir


def save_animation(
    anim, fps, file_name, file_type=".mp4", save_dir=None, save_anim=True
):
    # Get inputs if not passed
    if not save_dir:
        save_dir = get_default_plot_save_dir()
    # Save animation if indicated
    if save_anim:
        print(f"Saving {file_name}...")
        prev_dir = os.getcwd()
        os.chdir(save_dir)  # change to directory where saving
        writervideo = animation.FFMpegWriter(fps=fps)
        anim.save(f"{file_name}{file_type}", writer=writervideo)
        os.chdir(prev_dir)
