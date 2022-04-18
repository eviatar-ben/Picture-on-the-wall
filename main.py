import os
import io
import utilities
import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Acc.json'

IMAGES_PATH = 'Images'
THRESH = 0.5
DOMINANT_COLORS_NUM = 3
INPUT = r'Images\books1.jpeg'


def detect_properties(path, present=False):
    """Detects image properties in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation

    dominant_colors_3 = []
    i = 0
    for color in props.dominant_colors.colors:
        rgb = [color.color.red, color.color.green, color.color.blue, color.color.alpha]
        dominant_colors_3.append(utilities.closest_colour(rgb))
        i += 1
        # considering only the 4 most dominant colors
        if i > DOMINANT_COLORS_NUM:
            break
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
    return dominant_colors_3


def detect_labels(path, present=False):
    """Detects labels in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    detected_labels = []
    for label in labels:
        if label.score > THRESH:
            detected_labels.append(label.description)

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

    # no need to consider images without 'Picture frame' label - Noise
    if labels:
        df.loc[image] = pd.Series(process_labels_and_colors())


def load_data(images_list, df, cols):
    for image in images_list:
        image_path = f'{IMAGES_PATH}/{image}'
        get_and_insert_vector(image_path, image, cols, df)
    df.to_csv('TrainData')


def main():
    images_list = os.listdir(IMAGES_PATH)
    labels_cols = [label for label in utilities.relevant_labels]
    colors_cols = [color for color in utilities.relevant_colors]
    cols = set(labels_cols + colors_cols)
    df = pd.DataFrame(columns=cols, index=images_list)
    df.index.name = 'Image_name'
    load_data(images_list, df, cols)
    vector_to_predict = get_and_insert_vector(INPUT, None, cols, None, prediction=True)
    vector_to_predict.to_csv('vector_to_predict')


if __name__ == '__main__':
    main()
