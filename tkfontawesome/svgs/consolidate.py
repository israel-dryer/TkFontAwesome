"""Create svgs.py file from font-awesome icons directories.

brands, regular, solid should be copied into this directory from svgs directory
 in font awesome download zip.
icons.json should be copied into this directory from metadata directory in font
awesome download zip.
"""

import json
from pathlib import Path
from pprint import pformat

root = Path(__file__).parent

dirs = [root/'brands', root/'regular', root/'solid']

svg_dict = {}

for dir in dirs:
    print(dir)
    for file in dir.iterdir():
        svg_dict[file.stem] = file.read_text()


alias_dict = {}

with (root/'icons.json').open('r', encoding='utf8') as f:
   icons = json.load(f)

for icon, icon_data in icons.items():
    if 'aliases' not in icon_data or 'names' not in icon_data['aliases']:
        continue
    for alias in icon_data['aliases']['names']:
        alias_dict[alias] = icon

with (root/'..'/'svgs.py').open('w', encoding='utf-8') as f:
    f.write(f'FA = {pformat(svg_dict, width=9999, indent=4)}\nFA_aliases = {pformat(alias_dict, indent=4)}\n')
