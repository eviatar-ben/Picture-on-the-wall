import os
import cv2
import numpy

path = 'DATA1'
test_path = 'DATA2'
my_list = os.listdir(path)


def load_image_to_detect():
    image_to_detect = cv2.imread(f'{path}/judaica2.jpeg')
    return image_to_detect


def load_train_images():
    images = []
    images_names = []
    for cl in my_list:
        # todo maybe load with 0 - grayscale
        # img_cur = cv2.imread(f'{path}/{cl}', 0)

        img_cur = cv2.imread(f'{path}/{cl}')
        images.append(img_cur)
        images_names.append(os.path.splitext(cl)[0])

    return images, images_names


def find_des(images):
    desc_list = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        desc_list.append(des)
    return desc_list


def classify():
    pass


def find_id(img, desList, thres=15):
    cl = "judaica2.jpeg"
    img = cv2.imread(f'{test_path}/{cl}')
    kp2, des2 = orb.detectAndCompute(img, None)
    match_list = []
    final_val = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            match_list.append(len(good))
            # print(matchList)
    except:
        pass
    if len(match_list) != 0:
        if max(match_list) > thres:
            final_val = match_list.index(max(match_list))
    return final_val


if __name__ == '__main__':
    orb = cv2.ORB_create(nfeatures=1000)
    bf = cv2.BFMatcher()
    imgToDet = load_image_to_detect()
    train_images, class_names = load_train_images()
    des_list = find_des(train_images)
    i = find_id(imgToDet, des_list)
    print(class_names[i])
