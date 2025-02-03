import pyqrcode
from io import BytesIO
from base64 import b64encode
import numpy as np
import cv2

num_chars_per_qrcode = 33

sample_data_label = '''Congratulations, you've uncovered the mystery of the encoding algorithm; now continue solving the actual challenge!'''

flag = '42HN{u5in6_c0Lor_CH4nn3L5_tO_1NcR3453_D47a_d3NsI7y}'
challenge_success_label = '''Congratulations, you've done it! ''' + flag

def generate_random_qrcode(label):
	'''
	Generates and returns a QRCode (as base64-encoded data) with label as its data.
	'''
	# Split label in 3 roughly equally long parts
	assert len(label) > 2
	len_label = len(label)
	label_parts = [label[:len_label // 3], label[len_label // 3: len_label // 3 * 2], label[len_label // 3 * 2:]]
	assert ''.join(label_parts) == label
	
	# Generate a monochrome qr-codes
	qr_codes = [
		generate_qrcode(label_parts[0], np.array([0x00, 0x00, 0xFF])), # red
		generate_qrcode(label_parts[1], np.array([0x00, 0xFF, 0x00])), # green
		generate_qrcode(label_parts[2], np.array([0xFF, 0x00, 0x00])), # blue
	]
	result = qr_codes[0]
	
	# Overlay images:
	img_width = result.shape[1]
	img_height = result.shape[0]
	for rows_index in range(img_height):
		for cols_index in range(img_width):
			result[rows_index][cols_index][2] = qr_codes[0][rows_index][cols_index][2]
			result[rows_index][cols_index][1] = qr_codes[1][rows_index][cols_index][1]
			result[rows_index][cols_index][0] = qr_codes[2][rows_index][cols_index][0]
	# Return the base64 representation of the PNG byte array of the qr code image.
	return b64encode(cv2.imencode(".png", result)[1].tobytes()).decode()

def generate_qrcode(text, color):
	'''
	Returns the byte array representing the PNG of the qr code.
	'''
	# Generate black and white qr code
	qr = pyqrcode.create(text)
	buffer = BytesIO()
	qr.png(buffer, scale=10)
	qr_bytes = buffer.getvalue()
	# Convert qr code to cv2 colored image object
	nparr = np.fromstring(qr_bytes, np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
	img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
	# Color qr code monochrome
	img_width = img.shape[1]
	img_height = img.shape[0]
	for rows_index in range(img_height):
		for cols_index in range(img_width):
			if img[rows_index][cols_index][0] == 255:
				img[rows_index][cols_index] = color
	return img
