import random
import numpy as np
import cv2


# Create a random image
width = 1000
height = 100
shape = (height, width, 3)
random_image = np.zeros(shape, np.uint8)
# Fill the image with random data:
for y in range(height):
	for x in range(width):
		random_image[y, x, 0] = random.randint(0, 255)
		random_image[y, x, 1] = random.randint(0, 255)
		random_image[y, x, 2] = random.randint(0, 255)
# Write image to disk:
cv2.imwrite('random_image.png', random_image)

# Load flag image
flag_image = cv2.imread('flag.png')
assert flag_image.shape == shape

changes = []
for y in range(height):
	for x in range(width):
		diff = [(int(channel[0]) - int(channel[1])) for channel in zip(flag_image[y, x], random_image[y, x])]
		changes += [[y, x, diff]]
with open('changes.py', 'w') as f:
	f.write('changes = ' + str(changes))
