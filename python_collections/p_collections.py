from collections import namedtuple

# Namedtuple

Color = namedtuple("Color", ["red", "yellow", "green"])
color = Color("#FF0000", "#FFFF00", "#008000")
print(color.red)
print(color.yellow)
print(color.green)
