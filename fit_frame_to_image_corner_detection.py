import cv2
import numpy as np

OUTPUT_PATH = r"corner_detection_data"
INPUT = r'DATA\curtins1.jpeg'


def detect_corner():
    # Load image, grayscale, blur, Otsu's threshold

    image = cv2.imread(INPUT)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Find distorted bounding rect
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 5000:
            # Find distorted bounding rect
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.fillPoly(mask, [box], (255, 255, 255))

    # Find corners
    # Shi-Tomasi Corner Detector
    corners = cv2.goodFeaturesToTrack(mask, 100, .8, 100)
    offset = 15
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(image, (int(x), int(y)), 5, (36, 255, 12), -1)
        x, y = int(x), int(y)
        cv2.rectangle(image, (x - offset, y - offset), (x + offset, y + offset), (36, 255, 12), 3)
        print("({}, {})".format(x, y))

    cv2.imwrite(f"{OUTPUT_PATH}/thresh.jpg", thresh)
    cv2.imwrite(f"{OUTPUT_PATH}/img.jpg", image)
    cv2.imwrite(f"{OUTPUT_PATH}/mask.jpg", mask)


if __name__ == '__main__':
    detect_corner()
