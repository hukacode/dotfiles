import json

from os import path
from constant import theme_path

def load_theme():
    with open(path.join(theme_path)) as f:
        return json.load(f)

if __name__ == "theme":
    colors = load_theme()