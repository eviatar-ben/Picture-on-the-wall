# from imageai.Detection import ObjectDetection
import cv2
import os


def get_boxes_points(img):
    # execution_path = os.getcwd()
    #
    # detector = ObjectDetection()
    # detector.setModelTypeAsRetinaNet()
    # detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.1.0.h5"))
    # detector.loadModel()
    # detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, img),
    #                                              output_image_path=os.path.join(execution_path, "imagenew.jpg"))
    # box_points = []
    # for eachObject in detections:
    #     print(eachObject["name"], " : ", eachObject["percentage_probability"])
    #     print(f"box points: {eachObject['box_points']}")
    #     box_points.append(cv2.cv.BoxPoints(eachObject['box_points']))
    # return box_points
    pass


def get_empty_coord(box_points):
    x_margins = [b[0][0] - b[0][1] for b in box_points]
    y_margins = [b[1][0] - b[1][1] for b in box_points]

    return x_margins.index(max(x_margins)), y_margins.index(max(y_margins))


# test:
def get_coord(img):
    return 100, 200

# def get_coord(img):
#
#     return get_empty_coord(get_boxes_points(img))
