from pathlib import Path

root = Path(__file__).parent

dirs = [root/'brands', root/'regular', root/'solid']

svg_dict = {}

print(dirs[0])

for dir in dirs:
    for file in dir.iterdir():
        svg_dict[file.stem] = file.read_text()

with open(root / 'svgs.py', 'w', encoding='utf-8') as f:
    f.write(f'FA = {svg_dict}')