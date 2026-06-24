import cv2
import numpy as np

# Read source image
im_src = cv2.imread("C:/Users/Surendhar Reddy/Downloads/virat.jpg")

# Read destination image
im_dst = cv2.imread("C:/Users/Surendhar Reddy/Downloads/virat.jpg")

# Check images
if im_src is None:
    print("Error: Source image not found")
    exit()

if im_dst is None:
    print("Error: Destination image not found")
    exit()

# Source image dimensions
h_src, w_src = im_src.shape[:2]

# Four corners of source image
pts_src = np.array([
    [0, 0],
    [w_src - 1, 0],
    [w_src - 1, h_src - 1],
    [0, h_src - 1]
], dtype=np.float32)

# Location where Virat image should appear in destination image
pts_dst = np.array([
    [100, 100],   # Top-left
    [500, 100],   # Top-right
    [500, 600],   # Bottom-right
    [100, 600]    # Bottom-left
], dtype=np.float32)

# Compute Homography
h, status = cv2.findHomography(pts_src, pts_dst)

# Warp source image
im_out = cv2.warpPerspective(
    im_src,
    h,
    (im_dst.shape[1], im_dst.shape[0])
)

# Display images
cv2.imshow("Source Image", im_src)
cv2.imshow("Destination Image", im_dst)
cv2.imshow("Warped Source Image", im_out)

cv2.waitKey(0)
cv2.destroyAllWindows()
