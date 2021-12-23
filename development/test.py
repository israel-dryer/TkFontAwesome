from ctypes import windll

windll.user32.SetProcessDPIAware()

import tkinter as tk
from tkfontawesome import icon_to_image

root = tk.Tk()
fb = icon_to_image("facebook", fill="#4267B2", scale_to_width=64)
send = icon_to_image("paper-plane", fill="#1D9F75", scale_to_width=64)

tk.Label(root, image=fb).pack(padx=10, pady=10)
tk.Button(root, image=send).pack(padx=10, pady=10)

root.mainloop()
