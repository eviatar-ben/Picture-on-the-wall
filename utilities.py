import webcolors

# -----------------------------------------------------features------------------------------------------------------

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
    'Shelving',

]
all_labels = ['Clock', 'Real estate', 'Orange', 'Property', 'Bed frame', 'Skyscraper', 'Graphics', 'Yellow',
              'Flag of the united states', 'Line', 'Mountain', 'White', 'Flower', 'Pillow', 'Ceiling fixture',
              'Measuring instrument', 'Wall sticker', 'Visual arts', 'Poster', 'Lip', 'Circle', 'Amber', 'Tablecloth',
              'Aqua', 'Sports equipment', 'Coffee table', 'Style', 'Picnic basket', 'Bridal clothing', 'Couch',
              'Relief', 'Paint', 'Human leg', 'Comfort', 'Crankset', 'Screenshot', 'Tire', 'Room', 'Metal', 'Trunks',
              'Fruit', 'Organism', 'Wedding dress', 'Ecoregion', 'Artifact', 'Bicycles--Equipment and supplies',
              'Post-it note', 'Futon pad', 'Auto part', 'Bicycle stem', 'Symmetry', 'Twig', 'Home accessories',
              'Bicycle wheel', 'Hall', 'Interior design', 'Automotive wheel system', 'Logo', 'Product', 'Font',
              'Automotive tire', 'Still life photography', 'Roof', 'Anthropology', 'Triangle', 'Jewellery', 'Neck',
              'Pattern', 'Floor', 'Bicycle wheel rim', 'Armrest', 'Tent', 'Automotive exterior', 'Parallel',
              'Houseplant', 'Symbol', 'Window', 'Snapshot', 'Hearth', 'Leg', 'Gadget', 'Lighting', 'Collection',
              'Nature', 'Sharing', 'Computer', 'Stairs', 'Outdoor bench', 'Pink', 'Flag', 'Bicycle', 'Desk', 'Textile',
              'Beauty', 'Sofa bed', 'Street light', 'Shelving', 'Wood stain', 'Vision care', 'Art paint', 'Living room',
              'Grey', 'Lamp', 'Composite material', 'Sculpture', 'Herb', 'Head', 'Whiteboard', 'Slope', 'Watercraft',
              'Electronic device', 'Flooring', 'Snow', 'House', 'Ceiling', 'Hairstyle', 'Selfie', 'Table', 'Painting',
              'Sleeve', 'Computer desk', 'Water', 'Hardwood', 'Plastic', 'Outdoor furniture', 'Flowerpot',
              'Audio equipment', 'Event', 'Green', 'Plywood', 'Monochrome photography', 'Shelf', 'Face',
              'Automotive lighting', 'Eyewear', 'Petal', 'Electric blue', 'Vase', 'Tableware', 'Cabinetry', 'Happy',
              'Output device', 'Bicycle part', 'Design', 'Vertebrate', 'Peach', 'Decoration', 'Wall',
              'Automotive design', 'Linens', 'studio couch', 'Gesture', 'Eye', 'Religious item', 'Glasses',
              'Bicycle handlebar', 'Portable communications device', 'Material property', 'Bed', 'Bicycle hub',
              'Bicycle accessory', 'Plant', 'Rectangle', 'Grass', 'Art', 'Drawing', 'World', 'Shade', 'Botany',
              'Bicycle fork', 'Drawer', 'Bedroom', 'Dishware', 'Airplane', 'Display device', 'Motif', 'Serveware',
              'Office chair', 'Outdoor sofa', 'Leaf', 'Natural landscape', 'Bride', 'Paper', 'Shorts', 'Bunk bed',
              'Mirror', 'Beige', 'Fashion accessory', 'Kitchen & dining room table', 'Communication Device', 'Curtain',
              'Coat', 'Television', 'Furniture', 'Light', 'Door', 'Glass', 'Creative arts', 'Exhibition', 'Hub gear',
              'Hat', 'Cloud', 'Bicycle tire', 'Space', 'Brand', 'Black-and-white', 'Terrestrial plant', 'Drinkware',
              'Magenta', 'People on beach', 'Laminate flooring', 'Branch', 'Bedding', 'Clothing', 'Fixture', 'Facade',
              'Street fashion', 'Chair', 'Personal computer', 'Black', 'Fashion', 'Shirt', 'Dresser', 'Bicycle frame',
              'Mammal', 'Azure', 'Picture frame', 'Land vehicle', 'Beach', 'Ornament', 'Cross', 'Hair', 'Bookcase',
              'Line art', 'Ceiling fan', 'Electronic component', 'Tints and shades', 'Tree', 'Wheel', 'Cup', 'Vehicle',
              'Urban design', 'Dress', 'Smile', 'Illustration', 'Photograph', 'Formal wear', 'Bird', 'Wood', 'Laptop',
              'Oval', 'Club chair', 'Bermuda shorts', 'Architecture', 'Advertising', 'Gold', 'Natural material',
              'Watch', 'Bicycle seatpost', 'Map', 'Violet', 'Headgear', 'Outdoor table', 'Rim', 'Diagram',
              'Flash photography', 'Blue', 'Cheek', 'Facial expression', 'Brown', 'Aircraft', 'Boat', 'Purple', 'Sky',
              'Television set', 'Building', 'Umbrella']

labels_dicts = {label: 0 for label in all_labels}

colors_dict = {color: 0 for color in webcolors.CSS3_NAMES_TO_HEX.keys()}

colors_distribution = {'aliceblue': 4, 'antiquewhite': 25, 'aqua': 0, 'aquamarine': 0, 'azure': 0, 'beige': 8,
                       'bisque': 5, 'black': 160,
                       'blanchedalmond': 3, 'blue': 0, 'blueviolet': 0, 'brown': 21, 'burlywood': 26, 'cadetblue': 8,
                       'chartreuse': 0,
                       'chocolate': 9, 'coral': 4, 'cornflowerblue': 4, 'cornsilk': 1, 'crimson': 2, 'cyan': 0,
                       'darkblue': 0,
                       'darkcyan': 2, 'darkgoldenrod': 13, 'darkgray': 118, 'darkgrey': 0, 'darkgreen': 2,
                       'darkkhaki': 46,
                       'darkmagenta': 0, 'darkolivegreen': 139, 'darkorange': 0, 'darkorchid': 0, 'darkred': 1,
                       'darksalmon': 6,
                       'darkseagreen': 7, 'darkslateblue': 6, 'darkslategray': 218, 'darkslategrey': 0,
                       'darkturquoise': 0,
                       'darkviolet': 0, 'deeppink': 0, 'deepskyblue': 0, 'dimgray': 144, 'dimgrey': 0, 'dodgerblue': 1,
                       'firebrick': 13,
                       'floralwhite': 0, 'forestgreen': 0, 'fuchsia': 0, 'gainsboro': 158, 'ghostwhite': 0, 'gold': 1,
                       'goldenrod': 8,
                       'gray': 119, 'grey': 0, 'green': 0, 'greenyellow': 0, 'honeydew': 0, 'hotpink': 0,
                       'indianred': 22, 'indigo': 0,
                       'ivory': 0, 'khaki': 12, 'lavender': 34, 'lavenderblush': 0, 'lawngreen': 0, 'lemonchiffon': 0,
                       'lightblue': 2,
                       'lightcoral': 3, 'lightcyan': 0, 'lightgoldenrodyellow': 0, 'lightgray': 52, 'lightgrey': 0,
                       'lightgreen': 0,
                       'lightpink': 3, 'lightsalmon': 1, 'lightseagreen': 1, 'lightskyblue': 0, 'lightslategray': 8,
                       'lightslategrey': 0,
                       'lightsteelblue': 6, 'lightyellow': 0, 'lime': 0, 'limegreen': 0, 'linen': 126, 'magenta': 0,
                       'maroon': 31,
                       'mediumaquamarine': 1, 'mediumblue': 0, 'mediumorchid': 0, 'mediumpurple': 0,
                       'mediumseagreen': 0,
                       'mediumslateblue': 0, 'mediumspringgreen': 0, 'mediumturquoise': 2, 'mediumvioletred': 1,
                       'midnightblue': 5,
                       'mintcream': 0, 'mistyrose': 2, 'moccasin': 0, 'navajowhite': 2, 'navy': 0, 'oldlace': 0,
                       'olive': 0,
                       'olivedrab': 12, 'orange': 1, 'orangered': 0, 'orchid': 0, 'palegoldenrod': 3, 'palegreen': 0,
                       'paleturquoise': 1,
                       'palevioletred': 1, 'papayawhip': 0, 'peachpuff': 0, 'peru': 50, 'pink': 0, 'plum': 0,
                       'powderblue': 0,
                       'purple': 1, 'red': 0, 'rosybrown': 167, 'royalblue': 0, 'saddlebrown': 96, 'salmon': 3,
                       'sandybrown': 7,
                       'seagreen': 0, 'seashell': 4, 'sienna': 83, 'silver': 318, 'skyblue': 2, 'slateblue': 0,
                       'slategray': 16,
                       'slategrey': 0, 'snow': 8, 'springgreen': 0, 'steelblue': 5, 'tan': 68, 'teal': 3, 'thistle': 3,
                       'tomato': 2,
                       'turquoise': 1, 'violet': 0, 'wheat': 3, 'white': 3, 'whitesmoke': 95, 'yellow': 1,
                       'yellowgreen': 3}

filtered_colors = {k: v for k, v in colors_distribution.items() if v >= 3}

labels_distribution = {'Clock': 4, 'Real estate': 9, 'Orange': 62, 'Property': 400, 'Bed frame': 102, 'Skyscraper': 1,
                       'Graphics': 5, 'Yellow': 43, 'Flag of the united states': 1, 'Line': 47, 'Mountain': 1,
                       'White': 153, 'Flower': 21, 'Pillow': 48, 'Ceiling fixture': 1, 'Measuring instrument': 1,
                       'Wall sticker': 19, 'Visual arts': 6, 'Poster': 1, 'Lip': 1, 'Circle': 17, 'Amber': 1,
                       'Tablecloth': 2, 'Aqua': 2, 'Sports equipment': 2, 'Coffee table': 1, 'Style': 9,
                       'Picnic basket': 1, 'Bridal clothing': 1, 'Couch': 253, 'Relief': 1, 'Paint': 18, 'Human leg': 1,
                       'Comfort': 365, 'Crankset': 9, 'Screenshot': 2, 'Tire': 15, 'Room': 11, 'Metal': 6, 'Trunks': 1,
                       'Fruit': 1, 'Organism': 3, 'Wedding dress': 1, 'Ecoregion': 1, 'Artifact': 1,
                       'Bicycles--Equipment and supplies': 12, 'Post-it note': 1, 'Futon pad': 1, 'Auto part': 4,
                       'Bicycle stem': 1, 'Symmetry': 8, 'Twig': 24, 'Home accessories': 2, 'Bicycle wheel': 11,
                       'Hall': 3, 'Interior design': 550, 'Automotive wheel system': 1, 'Logo': 6, 'Product': 182,
                       'Font': 77, 'Automotive tire': 1, 'Still life photography': 1, 'Roof': 2, 'Anthropology': 1,
                       'Triangle': 5, 'Jewellery': 3, 'Neck': 1, 'Pattern': 18, 'Floor': 168, 'Bicycle wheel rim': 9,
                       'Armrest': 14, 'Tent': 1, 'Automotive exterior': 4, 'Parallel': 7, 'Houseplant': 99, 'Symbol': 3,
                       'Window': 130, 'Snapshot': 1, 'Hearth': 1, 'Leg': 1, 'Gadget': 1, 'Lighting': 167,
                       'Collection': 1, 'Nature': 5, 'Sharing': 2, 'Computer': 4, 'Stairs': 1, 'Outdoor bench': 1,
                       'Pink': 3, 'Flag': 1, 'Bicycle': 14, 'Desk': 4, 'Textile': 206, 'Beauty': 1, 'Sofa bed': 4,
                       'Street light': 1, 'Shelving': 39, 'Wood stain': 9, 'Vision care': 1, 'Art paint': 1,
                       'Living room': 92, 'Grey': 106, 'Lamp': 30, 'Composite material': 4, 'Sculpture': 2, 'Herb': 1,
                       'Head': 2, 'Whiteboard': 1, 'Slope': 4, 'Watercraft': 1, 'Electronic device': 1, 'Flooring': 151,
                       'Snow': 1, 'House': 34, 'Ceiling': 12, 'Hairstyle': 1, 'Selfie': 1, 'Table': 277, 'Painting': 7,
                       'Sleeve': 7, 'Computer desk': 4, 'Water': 2, 'Hardwood': 36, 'Plastic': 1,
                       'Outdoor furniture': 17, 'Flowerpot': 81, 'Audio equipment': 1, 'Event': 16, 'Green': 73,
                       'Plywood': 2, 'Monochrome photography': 1, 'Shelf': 17, 'Face': 1, 'Automotive lighting': 1,
                       'Eyewear': 1, 'Petal': 3, 'Electric blue': 4, 'Vase': 9, 'Tableware': 5, 'Cabinetry': 38,
                       'Happy': 2, 'Output device': 3, 'Bicycle part': 1, 'Design': 3, 'Vertebrate': 4, 'Peach': 1,
                       'Decoration': 85, 'Wall': 65, 'Automotive design': 12, 'Linens': 4, 'studio couch': 44,
                       'Gesture': 8, 'Eye': 1, 'Religious item': 1, 'Glasses': 1, 'Bicycle handlebar': 6,
                       'Portable communications device': 1, 'Material property': 22, 'Bed': 29, 'Bicycle hub': 3,
                       'Bicycle accessory': 1, 'Plant': 358, 'Rectangle': 466, 'Grass': 3, 'Art': 97, 'Drawing': 4,
                       'World': 1, 'Shade': 30, 'Botany': 2, 'Bicycle fork': 3, 'Drawer': 25, 'Bedroom': 1,
                       'Dishware': 7, 'Airplane': 1, 'Display device': 1, 'Motif': 1, 'Serveware': 7, 'Office chair': 1,
                       'Outdoor sofa': 1, 'Leaf': 8, 'Natural landscape': 1, 'Bride': 1, 'Paper': 1, 'Shorts': 2,
                       'Bunk bed': 1, 'Mirror': 13, 'Beige': 8, 'Fashion accessory': 5,
                       'Kitchen & dining room table': 2, 'Communication Device': 1, 'Curtain': 5, 'Coat': 1,
                       'Television': 1, 'Furniture': 614, 'Light': 31, 'Door': 11, 'Glass': 5, 'Creative arts': 2,
                       'Exhibition': 1, 'Hub gear': 1, 'Hat': 2, 'Cloud': 1, 'Bicycle tire': 8, 'Space': 3, 'Brand': 5,
                       'Black-and-white': 5, 'Terrestrial plant': 7, 'Drinkware': 1, 'Magenta': 2, 'People on beach': 1,
                       'Laminate flooring': 1, 'Branch': 29, 'Bedding': 3, 'Clothing': 1, 'Fixture': 13, 'Facade': 3,
                       'Street fashion': 1, 'Chair': 143, 'Personal computer': 1, 'Black': 72, 'Fashion': 1, 'Shirt': 1,
                       'Dresser': 1, 'Bicycle frame': 10, 'Mammal': 3, 'Azure': 80, 'Picture frame': 363,
                       'Land vehicle': 4, 'Beach': 1, 'Ornament': 3, 'Cross': 2, 'Hair': 1, 'Bookcase': 5,
                       'Line art': 1, 'Ceiling fan': 2, 'Electronic component': 1, 'Tints and shades': 8, 'Tree': 12,
                       'Wheel': 15, 'Cup': 1, 'Vehicle': 6, 'Urban design': 2, 'Dress': 1, 'Smile': 1,
                       'Illustration': 8, 'Photograph': 40, 'Formal wear': 1, 'Bird': 1, 'Wood': 597, 'Laptop': 1,
                       'Oval': 1, 'Club chair': 1, 'Bermuda shorts': 1, 'Architecture': 39, 'Advertising': 2, 'Gold': 2,
                       'Natural material': 8, 'Watch': 1, 'Bicycle seatpost': 5, 'Map': 2, 'Violet': 4, 'Headgear': 1,
                       'Outdoor table': 2, 'Rim': 1, 'Diagram': 1, 'Flash photography': 2, 'Blue': 33, 'Cheek': 1,
                       'Facial expression': 1, 'Brown': 57, 'Aircraft': 1, 'Boat': 1, 'Purple': 26, 'Sky': 1,
                       'Television set': 1, 'Building': 300, 'Umbrella': 1}

filtered_labels = {k: v for k, v in labels_distribution.items() if v >= 3}



# -----------------------------------------------------functions------------------------------------------------------
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
