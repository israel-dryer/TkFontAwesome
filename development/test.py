from tkfontawesome import icon_to_image
import tkinter as tk
from ctypes import windll

windll.user32.SetProcessDPIAware()

root = tk.Tk()
img = icon_to_image("facebook", fill="#4267B2", scale_to_width=64)

tk.Label(root, image=img).pack(padx=10, pady=10)

root.mainloop()
