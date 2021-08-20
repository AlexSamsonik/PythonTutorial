from collections import ChainMap

# ChainMap

parts = {
    "part_01": 1,
    "part_02": 2
}

options = {
    "options_01": 1,
    "part_01": 3,
    "part_02": 4
}

accessories = {
    "accessories_01": 1,
    "part_01": 5,
    "part_02": 6
}

pricing = ChainMap(accessories, parts, options)
print(pricing.get("part_02"))
print(pricing.get("part_01"))
