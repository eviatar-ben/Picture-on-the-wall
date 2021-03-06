import os
import io
import utilities
import pandas as pd
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Acc.json'

IMAGES_PATH = r'all_images'
THRESH = 0.5
DOMINANT_COLORS_NUM = 4
INPUT = r'Images\curtins1.jpeg'

all_labels = []


def detect_properties(path, present=False):
    """Detects image properties in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation

    dominant_colors_4 = []
    i = 0
    for color in props.dominant_colors.colors:
        rgb = [color.color.red, color.color.green, color.color.blue, color.color.alpha]
        projected_color = utilities.closest_colour(rgb)
        if projected_color in utilities.filtered_colors.keys():
            dominant_colors_4.append(projected_color)
        i += 1
        # considering only the 4 most dominant colors
        if i > DOMINANT_COLORS_NUM:
            break
        # in order to minimize bias-variance trade off research for noisy features is needed
        utilities.colors_dict[projected_color] += 1
    if present:
        print('Properties:')
        for color in props.dominant_colors.colors:
            print('fraction: {}'.format(color.pixel_fraction))
            print('\tr: {}'.format(color.color.red))
            print('\tg: {}'.format(color.color.green))
            print('\tb: {}'.format(color.color.blue))
            print('\ta: {}'.format(color.color.alpha))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return dominant_colors_4


def detect_labels(path, present=False):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    detected_labels = []
    for label in labels:
        all_labels.append(label.description)
        if label.score > THRESH and label.description in utilities.filtered_labels.keys():
            detected_labels.append(label.description)

        # in order to minimize bias-variance trade off research for noisy features is needed
        utilities.labels_dicts[label.description] += 1

    if present:
        print('Labels:')
        for label in labels:
            print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    # no need to consider images without 'Picture frame' label - Noise
    if 'Picture frame' not in detected_labels:
        return
    return detected_labels


def get_and_insert_vector(image_path, image, cols, df, prediction=False):
    """
    get the image's vector and set it in the TrainData Frame df.
    if prediction is True meaning the given image is the input.

    return the df, in case that image frame didnt detect the df will drop the proper  redundant row.
    in case which prediction is needed the vector will be returned
    """

    def process_labels_and_colors():

        result = {feature: False for feature in cols}
        for label in labels:
            if label in utilities.relevant_labels:
                result[label] = True
        for color in dominant_colors:
            if color in utilities.relevant_colors:
                result[color] = True
            else:
                print(f'error? {color} is not in relevant colors')
        return result

    dominant_colors = detect_properties(image_path)
    labels = detect_labels(image_path)

    if prediction:
        return pd.Series(process_labels_and_colors())
    # deleting the empty row
    if not labels:
        df = df.drop(image)
    # no need to consider images without 'Picture frame' label - Noise
    if labels:
        df.loc[image] = pd.Series(process_labels_and_colors())
    return df


def load_data(images_list, df, cols):
    i = 0
    for image in images_list:
        i += 1
        if i in [50, 100, 150, 200, 250, 300, 350, 400, 450]:
            print(utilities.labels_dicts)
            print(utilities.colors_dict)

        print(f"working on image: {image}")
        image_path = f'{IMAGES_PATH}/{image}'
        try:
            df = get_and_insert_vector(image_path, image, cols, df)
        except:
            print(f"exception in image {image}")

    df.to_csv('TrainData')
