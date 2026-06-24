import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Surendhar Reddy\Downloads\virat.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found. Check the file path.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Create High-Boost Mask
    mask = cv2.subtract(gray, blur)

    # Amplification factor
    A = 1.5

    # High-Boost Sharpening
    high_boost = cv2.addWeighted(gray, A, mask, 1, 0)

    # Display images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Blurred Image", blur)
    cv2.imshow("High-Boost Sharpened Image", high_boost)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
