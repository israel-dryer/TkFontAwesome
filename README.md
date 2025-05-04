[![PyPI](https://img.shields.io/pypi/v/tkfontawesome.svg)](https://pypi.org/project/tkfontawesome/)
[![Downloads](https://static.pepy.tech/badge/tkfontawesome/month)](https://pepy.tech/project/tkfontawesome)
[![GitHub issues](https://img.shields.io/github/issues/israel-dryer/tkfontawesome.svg)](https://github.com/israel-dryer/tkfontawesome/issues)
[![GitHub issues closed](https://img.shields.io/github/issues-closed/israel-dryer/tkfontawesome.svg)](https://github.com/israel-dryer/tkfontawesome/issues?q=is%3Aissue+is%3Aclosed)
[![License](https://img.shields.io/github/license/israel-dryer/tkfontawesome.svg)](https://github.com/israel-dryer/tkfontawesome/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/israel-dryer/tkfontawesome.svg)](https://github.com/israel-dryer/tkfontawesome/stargazers)
[![Forks](https://img.shields.io/github/forks/israel-dryer/tkfontawesome.svg)](https://github.com/israel-dryer/tkfontawesome/network)
[![Code Size](https://img.shields.io/github/languages/code-size/israel-dryer/tkfontawesome)](https://github.com/israel-dryer/tkfontawesome)

# TkFontAwesome

> Requires Python **3.8+**

A library that enables you to use [FontAwesome icons](https://fontawesome.com/v6/icons?o=r&m=free)
in your tkinter application.

You may use any of the 2k+ *free* [FontAwesome 6.5 icons](https://fontawesome.com/v6/icons?o=r&m=free).
The **fill color** and **size** are customized to your specifications and then converted
to an object via [tksvg](https://pypi.org/project/tksvg/) that can be used anywhere you would use a `tkinter.PhotoImage` object.

![example-2](https://raw.githubusercontent.com/israel-dryer/TkFontAwesome/main/assets/example-2.png)

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

![example-1](https://raw.githubusercontent.com/israel-dryer/TkFontAwesome/main/assets/example-1.png)

## API: `icon_to_image()`

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
|-------------------|-------|-----------------------------------------------------------------------|-----------|
| name              | str   | The name of the FontAwesome icon.                                     | None      |
| fill              | str   | The fill color of the svg path.                                       | None      |
| scale_to_width    | int   | Adjust image width to this size (in pixels); maintains aspect ratio.  | None      |
| scale_to_height   | int   | Adjust image height to this size (in pixels); maintains aspect ratio. | None      |
| scale             | float | Scale the image width and height by this factor.                      | 1         |

## License

The [CC BY 4.0](https://fontawesome.com/license/free) license applies to all FontAwesome *free* icons used in the library.
The MIT License applies to all other work.

---

**Author**: [Israel Dryer](https://github.com/israel-dryer)
📦 Available on [PyPI](https://pypi.org/project/tkfontawesome/) | 🐙 [GitHub](https://github.com/israel-dryer/tkfontawesome)
