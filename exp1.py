import cv2
image = cv2.imread("C:/Users/Surendhar Reddy/Downloads/hd-nature-trees-and-river-8rfx5pdyjung0qf0.jpg")
cv2.imshow("Original Image", image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
