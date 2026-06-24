import cv2
import numpy as np

image = cv2.imread("C:/Users/Surendhar Reddy/Downloads/virat.jpg")

h, w = image.shape[:2]

canvas_h = 1000
canvas_w = 1500

x, y = 100, 100
dx, dy = 5, 3

while True:

    if x + w >= canvas_w or x <= 0:
        dx = -dx

    if y + h >= canvas_h or y <= 0:
        dy = -dy

    x += dx
    y += dy

    canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)

    canvas[y:y+h, x:x+w] = image

    cv2.imshow("Moving Image", canvas)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
