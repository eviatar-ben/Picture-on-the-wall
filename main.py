import vision_and_data_tools
import KNNeighborsClassifier
import os
import pandas as pd

import csv

INDEX_NAME = 'Image_name'
IMAGES_PATH = r'all_images'
INPUT = r'Images\books1.jpeg'


def main():
    images_list = os.listdir(vision_and_data_tools.IMAGES_PATH)
    labels_cols = [label for label in vision_and_data_tools.utilities.relevant_labels]
    colors_cols = [color for color in vision_and_data_tools.utilities.relevant_colors]
    cols = set(labels_cols + colors_cols)
    df = pd.DataFrame(columns=cols, index=images_list)
    df.index.name = INDEX_NAME
    vision_and_data_tools.load_data(images_list, df, cols)
    vector_to_predict = vision_and_data_tools.get_and_insert_vector(vision_and_data_tools.INPUT, None, cols, None,
                                                                    prediction=True)
    vector_to_predict.to_csv('vector_to_predict')
    KNNeighborsClassifier.get_prediction()

    l_df = pd.DataFrame(vision_and_data_tools.all_labels)
    l_df.to_csv("all_labels.csv")


if __name__ == '__main__':

    main()
    print(vision_and_data_tools.utilities.labels_dicts)
    print(vision_and_data_tools.utilities.colors_dict)
    with open('dict.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in vision_and_data_tools.utilities.labels_dicts.items():
            writer.writerow([key, value])

        for key, value in vision_and_data_tools.utilities.colors_dict.items():
            writer.writerow([key, value])

