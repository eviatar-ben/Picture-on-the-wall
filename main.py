import vision_and_data_tools
import KNNeighborsClassifier
import os
import pandas as pd

INDEX_NAME = 'Image_name'


def main():
    images_list = os.listdir(vision_and_data_tools.IMAGES_PATH)
    labels_cols = [label for label in vision_and_data_tools.utilities.relevant_labels]
    colors_cols = [color for color in vision_and_data_tools.utilities.relevant_colors]
    cols = set(labels_cols + colors_cols)
    df = pd.DataFrame(columns=cols, index=images_list)
    df.index.name = INDEX_NAME
    vision_and_data_tools.load_data(images_list, df, cols)
    vector_to_predict = vision_and_data_tools.get_and_insert_vector(vision_and_data_tools.INPUT, None, cols, None, prediction=True)
    vector_to_predict.to_csv('vector_to_predict')

    KNNeighborsClassifier.get_prediction()


if __name__ == '__main__':
    main()
