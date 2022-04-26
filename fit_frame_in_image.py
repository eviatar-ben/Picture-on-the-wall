from PIL import Image, ImageDraw, ImageFilter

import yolo_detector
import cv2


def fit_frame(img):
    x, y = yolo_detector.get_coord(img)
    # -----test:-----
    im1 = Image.open(img)

    # resize frame to image's sizes
    im2 = Image.open('ROI_1.jpg')
    basewidth = 600
    wpercent = (basewidth / float(im2.size[0]))
    hsize = int((float(im2.size[1]) * float(wpercent)))
    im2 = im2.resize((basewidth, hsize), Image.ANTIALIAS)

    im1.paste(im2, (x, y))
    im1.save('final_result.jpg', quality=95)
