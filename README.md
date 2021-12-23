# TkFontAwesome

A library that enables you to use [FontAwesome icons](https://fontawesome.com/v5.0/icons?d=gallery&p=2&m=free) 
in your tkinter application. 

You may use any of the 1k+ _free_ [FontAwesome 5.0 icons](https://fontawesome.com/v5.0/icons?d=gallery&m=free). 
The **fill color** and **size** are customized to your specifications and then converted
to an object via [tksvg](https://pypi.org/project/tksvg/) that can be used anywhere you would use a `tkinter.PhotoImage` object.

![example-2](https://raw.githubusercontent.com/israel-dryer/TkFontAwesome/main/assets/example-2.1.png)

## Installation

```shell
python -m pip install tkfontawesome
```

## Usage

```python
import tkinter as tk
from tkfontawesome import icon_to_image

root = tk.Tk()
fb = icon_to_image("facebook", fill="#4267B2", scale_to_width=64)
send = icon_to_image("paper-plane", fill="#1D9F75", scale_to_width=64)

tk.Label(root, image=fb).pack(padx=10, pady=10)
tk.Button(root, image=send).pack(padx=10, pady=10)

root.mainloop()
```

![example-1](https://raw.githubusercontent.com/israel-dryer/TkFontAwesome/main/assets/example-1.1.png)

## tkfontawesome.`icon_to_image`
```python
(
    name=None, 
    fill=None, 
    scale_to_width=None, 
    scale_to_height=None, 
    scale=1
)
```

### Parameters
| Name              | Type  | Description                                                           | Default   |
| ---               | ---   | ---                                                                   | ---       | 
| name              | str   | The name of the FontAwesome icon.                                     | None |
| fill              | str   | The fill color of the svg path.                                       | None |
| scale_to_width    | int   | Adjust image width to this size (in pixels); maintains aspect ratio.  | None |
| scale_to_height   | int   | Adjust image height to this size (in pixels); maintains aspect ratio. | None |
| scale             | float | Scale the image width and height by this factor.                      | 1 |

## License

The [CC BY 4.0](https://fontawesome.com/license/free) license applies to all FontAwesome _free_ icons used in the library.
The MIT License applies to all other work.
