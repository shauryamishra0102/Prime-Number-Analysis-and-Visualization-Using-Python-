# utils.py

import os

def ensure_folders():
    folders = [
        "assets",
        "assets/saved_plots",
        "assets/gifs",
        "assets/examples"
    ]

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
