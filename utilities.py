import webcolors

relevant_colors = [color for color in webcolors.CSS3_NAMES_TO_HEX.keys()]
relevant_labels = [
    'Picture frame',
    'Textile',
    'Paint',
    'Flowerpot',
    'Comfort',
    'Wood',
    'Rectangle',
    'Art',
    'Aqua',
    'Flooring',
    'Interior design',
    'Paint',
    'Creative arts',
    'Painting',
    'Textile',
    'Window',
    'Floor',
    'Musical instrument',
    'Plant',
    'Visual arts'
    'Exhibition',
    'Picture frame',
    'Door',
    'Shelving'
]


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
