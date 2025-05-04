import tkinter as tk
from tkfontawesome import icon_to_image

root = tk.Tk()
img = icon_to_image("facebook", fill="#4267B2", scale_to_width=64)
tk.Label(root, image=img).pack(padx=20, pady=20)
root.mainloop()
