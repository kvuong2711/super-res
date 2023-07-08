import cv2


def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    global ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        ix = x
        iy = y

        display_img = img.copy()
        cv2.circle(display_img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('image', display_img)


if __name__ == '__main__':
    # Write a script to load an input image, use cv2 to allow users to select a point on the image, and then crop the image around that point. The cropped image should be saved to disk.

    # Load an input image
    img_path = '/home/khiem/Downloads/iCloud Photos/IMG_5915.JPEG'
    img = cv2.imread(img_path)
    global ix, iy

    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # ix, iy = 751, 999

    # and then crop the image around that point.
    # print x, y coordinates
    print(ix, ' ', iy)

    cs = 32 // 2
    crop_img = img[iy - cs:iy + cs, ix - cs:ix + cs]
    # Resize to 64x64
    crop_img = cv2.resize(crop_img, (64, 64), interpolation=cv2.INTER_CUBIC)
    # Display cropped image
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)

    # The cropped image should be saved to disk.
    cv2.imwrite(img_path.replace('.JPEG', '_crop32up.JPEG'), crop_img)



