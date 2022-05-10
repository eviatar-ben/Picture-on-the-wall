import vision_and_data_tools
import KNNeighborsClassifier
import os
import pandas as pd
import yolo_detector
import csv
import fit_frame_in_image
import frame_detector

INDEX_NAME = 'Image_name'
IMAGES_PATH = r'all_images'
INPUT = r'Images\shelf2.jpeg'


def get_all_features():
    images_list = os.listdir(vision_and_data_tools.IMAGES_PATH)
    labels_cols = [label for label in vision_and_data_tools.utilities.relevant_labels]
    colors_cols = [color for color in vision_and_data_tools.utilities.relevant_colors]
    cols = set(labels_cols + colors_cols)
    df = pd.DataFrame(columns=cols, index=images_list)
    df.index.name = INDEX_NAME
    return cols, df, images_list


def main():
    import sys
    path_input = vision_and_data_tools.INPUT
    if len(sys.argv) > 1:
        path_input = sys.argv[1]
    # preprocess:
    cols, df, images_list = get_all_features()

    # Data is ready to use no need to rerun
    # vision_and_data_tools.load_data(images_list, df, cols)

    # get image feature vector (projection):
    vector_to_predict = vision_and_data_tools.get_and_insert_vector(path_input, None, cols, None,
                                                                    prediction=True)
    # get closest image to input:
    vector_to_predict.to_csv('vector_to_predict')
    prediction = KNNeighborsClassifier.get_prediction()[0]

    # show the region of interest according to the image's contours:
    frame_detector.show_region_of_interest()
    fit_frame_in_image.fit_frame(INPUT)


if __name__ == '__main__':
    main()
