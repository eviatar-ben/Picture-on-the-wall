import vision_and_data_tools
import KNNeighborsClassifier
import os
import pandas as pd
import yolo_detector
import csv

INDEX_NAME = 'Image_name'
IMAGES_PATH = r'all_images'
INPUT = r'Images\bed1.jpeg'


def main():
    images_list = os.listdir(vision_and_data_tools.IMAGES_PATH)
    labels_cols = [label for label in vision_and_data_tools.utilities.relevant_labels]
    colors_cols = [color for color in vision_and_data_tools.utilities.relevant_colors]
    cols = set(labels_cols + colors_cols)
    df = pd.DataFrame(columns=cols, index=images_list)
    df.index.name = INDEX_NAME
    # TrainData is ready to use
    # vision_and_data_tools.load_data(images_list, df, cols)
    vector_to_predict = vision_and_data_tools.get_and_insert_vector(vision_and_data_tools.INPUT, None, cols, None,
                                                                    prediction=True)
    vector_to_predict.to_csv('vector_to_predict')
    prediction = KNNeighborsClassifier.get_prediction()[0]

    most_likely = yolo_detector.get_empty_coord(yolo_detector.get_boxes_points("image.jpg"))

    l_df = pd.DataFrame(vision_and_data_tools.all_labels)
    l_df.to_csv("all_labels.csv")


if __name__ == '__main__':
    main()
