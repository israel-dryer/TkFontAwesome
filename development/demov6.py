from tkfontawesome import icon_to_image
import tkinter as tk
from ctypes import windll

windll.user32.SetProcessDPIAware()

icons = [
    (
        "x-twitter",
        "stapler",
        "fa-bridge-water",
        "envelope-circle-check",
        "hill-rockslide",
        "mobile-retro",
        "people-pulling",
        "person-cane",
    ),
    (
        "person-drowning",
        "person-walking-luggage",
        "ranking-star",
        "shield-heart",
        "toilets-portable",
        "panorama",
        "shrimp",
        "timeline",
    ),
    (
        "child-reaching",
        "mitten",
        "bowl-rice",
        "bucket",
        "cubes-stacked",
        "jug-detergent",
        "shield-dog",
        "bug-slash",
    ),
]

root = tk.Tk()
images = []

for i, row in enumerate(icons):
    root.rowconfigure(i, weight=1)
    for j, icon in enumerate(row):
        root.columnconfigure(j, weight=1)
        images.append(icon_to_image(icon, scale_to_width=64))
        tk.Label(root, image=images[-1]).grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
