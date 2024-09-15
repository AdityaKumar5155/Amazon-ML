import cv2
import numpy as np

# Load the image
image = cv2.imread('gray.jpg')

# Upscale the image (resize with cubic interpolation for better quality)
scale_percent = 300  # Percentage to upscale the image
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image using INTER_CUBIC interpolation
upscaled_image = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)

# Apply a Gaussian blur to smooth the pixelated areas
blurred_image = cv2.GaussianBlur(upscaled_image, (5, 5), 0)

# Sharpen the image using a kernel
kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
for i in range(20):
    sharpened_image = cv2.filter2D(blurred_image, -1, kernel)

# Save or display the final image
cv2.imwrite('fixed_image_gray.jpg', sharpened_image)

# Optionally, display the result
# cv2.imshow('Fixed Image', sharpened_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
