import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import cv2

INPUT_PATH = r'vector_to_predict'
DATA_PATH = r'TrainData_460'


def split_data(df):
    y = df.iloc[:, 0]
    x = df.iloc[:, 1:]
    return x.to_numpy(), y.to_numpy()


def get_prediction():
    import frame_detector
    df = pd.read_csv(DATA_PATH)
    x, y = split_data(df)
    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(x, y)
    v = pd.read_csv(INPUT_PATH, squeeze=True).iloc[:, 1:].to_numpy()

    prediction = classifier.predict(v.T)
    # print(prediction)

    cv2.namedWindow("prediction", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("prediction", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # -----test: ------
    # cv2.imshow("prediction", cv2.imread(r"all_images\42.colorful-dining-room-red-chairs.jpg"))
    # im = cv2.imread(f"all_images\{prediction[0]}")
    # cv2.imwrite(r"Images\shelf2_response.jpg", im)

    cv2.imshow("prediction", cv2.imread(f"all_images\{prediction[0]}"))
    cv2.waitKey()

    return prediction


if __name__ == '__main__':
    get_prediction()
