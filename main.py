from vision_and_data_tools import *
from KNNeighborsClassifier import *
import os


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

    get_prediction()

if __name__ == '__main__':
    main()
