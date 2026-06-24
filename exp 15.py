import cv2
import numpy as np

# Read images
img1 = cv2.imread("C:/Users/Surendhar Reddy/Downloads/virat.jpg")
img2 = cv2.imread("C:/Users/Surendhar Reddy/Downloads/MAX VERSTAPPEN.jpg")

# Check if images loaded successfully
if img1 is None or img2 is None:
    print("Error loading images")
    exit()

# Define corresponding points
pts1 = np.array([
    [50, 50],
    [200, 50],
    [50, 200],
    [200, 200]
], dtype=np.float32)

pts2 = np.array([
    [100, 100],
    [300, 100],
    [100, 300],
    [300, 300]
], dtype=np.float32)

# Compute Homography Matrix
H, status = cv2.findHomography(pts1, pts2)

# Apply Perspective Warp
dst = cv2.warpPerspective(
    img1,
    H,
    (img2.shape[1], img2.shape[0])
)

# Display images
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Warped Image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
