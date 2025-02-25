import numpy as np
import cv2

# Read the changes
from changes import changes

# Read the modified image
im = cv2.imread('random_image.png')

try:
	# Reconstruct the original image:
	for y, x, color_changes in changes:
		im[y, x, 0] = (color_changes[0] + im[y, x, 0]) if color_changes[0] >= 0 else (im[y, x, 0] - abs(color_changes[0]))
		im[y, x, 1] = (color_changes[1] + im[y, x, 1]) if color_changes[1] >= 0 else (im[y, x, 1] - abs(color_changes[1]))
		im[y, x, 2] = (color_changes[2] + im[y, x, 2]) if color_changes[2] >= 0 else (im[y, x, 2] - abs(color_changes[2]))
         
except:
	print(x,y)
	print(im[y, x])
	print(color_changes)

# Write the image to disk:
cv2.imwrite('reconstructed_flag.png', im)

# [Optional] Enhance readability by modifying the color scheme of the image:
for y in range(im.shape[0]):
	for x in range(im.shape[1]):
		# The flag font color is roughly RGB = (185, 122, 87)
		im[y, x] = np.array([0, 0, 0], np.uint8) if 170 <= im[y, x][2] <= 200 and 105 <= im[y, x][1] <= 140 and 70 <= im[y, x][0] <= 105 else np.array([255, 255, 255], np.uint8)
cv2.imwrite('reconstructed_enhanced_flag.png', im)