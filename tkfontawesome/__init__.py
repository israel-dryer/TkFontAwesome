import io
import tksvg
from lxml import etree
from tkfontawesome.svgs import FA, FA_aliases


def icon_to_image(name, fill=None, scale_to_width=None, scale_to_height=None, scale=1):
    """
    Look up a FontAwesome icon by name and return it as an SvgImage object,
    which can be used anywhere a PhotoImage object is used in tkinter.

    Parameters:
        name (str): Name of the FontAwesome icon (e.g., 'facebook').
        fill (str): Optional fill color for the icon (e.g., "#4267B2").
        scale_to_width (int): Target width in pixels (maintains aspect ratio).
        scale_to_height (int): Target height in pixels (maintains aspect ratio).
        scale (float): Scaling factor (applied only if width/height are not set).

    Returns:
        SvgImage: The converted SVG image ready for tkinter use.

    Example:
        import tkinter as tk
        from tkfontawesome import icon_to_image

        root = tk.Tk()
        img = icon_to_image("facebook", fill="#4267B2", scale_to_width=64)
        tk.Label(root, image=img).pack(padx=10, pady=10)
        root.mainloop()
    """
    name = FA_aliases.get(name, name)
    if name.startswith('fa-'):
        name = name[3:]
    xml_data = FA.get(name)
    if xml_data is None:
        raise ValueError(
            f"'{name}' is not a valid icon name. Check spelling or visit https://fontawesome.com/icons."
        )
    return svg_to_image(xml_data, fill, scale_to_width, scale_to_height, scale)


def svg_to_image(source, fill=None, scale_to_width=None, scale_to_height=None, scale=1):
    """
    Convert an SVG string into an SvgImage object for use in tkinter.

    Parameters:
        source (str): Raw SVG XML string.
        fill (str): Optional fill color override.
        scale_to_width (int): Width in pixels (maintains aspect ratio).
        scale_to_height (int): Height in pixels (maintains aspect ratio).
        scale (float): Optional scaling factor.

    Returns:
        SvgImage: The processed image object.
    """
    root = etree.fromstring(source)
    tree = etree.ElementTree(root)

    # Apply fill color override if provided
    if fill:
        for elem in root.iter():
            tag = str(elem.tag)
            if 'fill' in elem.attrib:
                elem.attrib['fill'] = fill
            elif tag.endswith("path"):
                elem.attrib['fill'] = fill

    img_data = io.BytesIO()
    tree.write(img_data)
    params = {"data": img_data.getvalue()}
    if scale_to_width:
        params["scaletowidth"] = scale_to_width
    if scale_to_height:
        params["scaletoheight"] = scale_to_height
    if scale != 1:
        params["scale"] = scale

    return tksvg.SvgImage(**params)
