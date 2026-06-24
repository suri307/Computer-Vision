import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Source points in webcam image
    imgPts = np.float32([
        [114, 151],
        [605, 89],
        [72, 420],
        [637, 420]
    ])

    # Destination points
    objPoints = np.float32([
        [0, 0],
        [420, 0],
        [0, 637],
        [420, 637]
    ])

    # Draw corner points
    for pt in imgPts:
        cv2.circle(frame, tuple(pt.astype(int)), 5, (0, 0, 255), -1)

    # Perspective transformation
    matrix = cv2.getPerspectiveTransform(imgPts, objPoints)

    result = cv2.warpPerspective(frame, matrix, (420, 637))

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Perspective Transformation", result)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
