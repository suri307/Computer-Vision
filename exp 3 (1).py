import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread(r"C:/Users/shaik/Downloads/0267bb844500aee50bd9d4e771c7029e.jpg")

if img is None:
    print("Image not found!")
else:
    img = cv2.resize(img, (600, 600))
    cv2.imshow("Image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
