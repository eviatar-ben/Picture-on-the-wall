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
    'Shelving'
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
