import cv2
import numpy as np
image=cv2.imread("C:/Users/Surendhar Reddy/Downloads/Virat-Kohli-4.webp")
kernel=np.ones((5,5),np.uint8)
eroded_image=cv2.erode(image,kernel,iterations=1)
cv2.imshow('original image',image)
cv2.imshow('eroded image',eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
