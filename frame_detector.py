import cv2
import numpy as np

IMG = r"all_images"


def show_frame_in_image(img):
    # Load image, grayscale, median blur, sharpen image
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

    # Threshold and morph close
    thresh = cv2.threshold(sharpen, 160, 255, cv2.THRESH_BINARY_INV)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find contours and filter using threshold area
    cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    min_area = 100
    max_area = 1500
    image_number = 0
    for c in cnts:
        area = cv2.contourArea(c)
        if area > min_area and area < max_area:
            x, y, w, h = cv2.boundingRect(c)
            ROI = image[y:y + h, x:x + w]
            cv2.imwrite(f'ROI_{image_number}.jpg', ROI)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
            image_number += 1

    # cv2.namedWindow("sharpen", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("sharpen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.imshow('sharpen', sharpen)
    # cv2.namedWindow("close", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("close", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.imshow('close', close)
    # cv2.namedWindow("thresh", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("thresh", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('thresh', thresh)
    # cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.imshow(f'image{img}', image)
    # cv2.imwrite(r'final\region_of_interest.jpg', image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def show_region_of_interest(img=None):
    # test:
    if not img:
        img  = r'all_images\42.colorful-dining-room-red-chairs.jpg'

    show_frame_in_image(f"{img}")


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join

    # ---------------------------------------- testing:---------------------------------------------

    # imgs = [f for f in listdir(IMG) if isfile(join(IMG, f))]
    imgs = [
        '91.51pd1eg7wvl._ss510_.jpg',
        '55.the-over-the-sofa-classic-gallery-frames-set-set-of-7-z.jpg',
        '91.depositphotos_279894702-stock-photo-stylish-scandi-interior-home-space.jpg',
        '42.colorful-dining-room-red-chairs.jpg',
        '48.stylish-scandi-interior-of-home-space-with-design-grey-sofa-and-retro-picture-id1141409483.jpg',
        '1.stylish-retro-interior-of-living-room-with-design-sofa-pillow-and-up-picture-id1130536777.jpg',
        '12.unique-living-room-in-modern-style-interior-with-design-sofa-elegant-picture-id1290048769.jpg',
        '24.s-l300.jpg',
        '28.vertical-modern-interior-bedroom-living-room-eclectic-wall-empty-frame-copyspace-drawing-d-rendering-modern-design-98970620.jpg',
        '30.14pcs-wood-picture-frames-for-wall-hanging-classic-photo-frame-wall-with-picture-wooden-frame-for.jpg_q90.jpg_.webp',
        '59.retro-style-home-decor-for-wall.jpg',
        '60.66644.jpg',
        '60.66644.jpg',
        '61.interior-vintage-design-of-nice-girly-bedroom-picture-id470450217.jpg',
        '76.depositphotos_311144980-stock-photo-stylish-bohemian-interior-design-living.jpg',
        '87.s-l300.jpg',
        '93.5e215836a77fd20241a57001-large.jpg',
        '96.c870x524.jpg']
    imgs = ['42.colorful-dining-room-red-chairs.jpg']
    for img in imgs:
        show_frame_in_image(f"{IMG}\{img}")
        print(img)
