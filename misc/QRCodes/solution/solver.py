# Additionally required packages for the python3-bookworm docker container to run this code. (docker run --rm -it python:bookworm /bin/bash)
#apt update && apt install -y libzbar0 ffmpeg libsm6 libxext6
#pip install pyzbar pypng opencv-python numpy pwntools

from pwn import remote # pip install pwntools
from pyzbar import pyzbar # pip install pyzbar
import numpy as np # pip install numpy
import cv2 # pip install opencv-python
from base64 import b64decode


host = '192.214.171.83' #'localhost'
port = 3002 #8448


def decode_img(img):
	'''
	Splits the image in 3 color channels, converts them to black and white and decodes the individual qr codes.
	'''
	result = ''
	# decode red color channel:
	img_channel_red = img.copy()
	img_width = img_channel_red.shape[1]
	img_height = img_channel_red.shape[0]
	for rows_index in range(img_height):
		for cols_index in range(img_width):
			img_channel_red[rows_index][cols_index][0] = img_channel_red[rows_index][cols_index][2]
			img_channel_red[rows_index][cols_index][1] = img_channel_red[rows_index][cols_index][2]
	img_channel_red = cv2.cvtColor(img_channel_red, cv2.COLOR_BGR2GRAY)
	result += [result.data.decode() for result in pyzbar.decode(image=img_channel_red)][0]
	# decode green color channel:
	img_channel_green = img.copy()
	img_width = img_channel_green.shape[1]
	img_height = img_channel_green.shape[0]
	for rows_index in range(img_height):
		for cols_index in range(img_width):
			img_channel_green[rows_index][cols_index][0] = img_channel_green[rows_index][cols_index][1]
			img_channel_green[rows_index][cols_index][2] = img_channel_green[rows_index][cols_index][1]
	img_channel_green = cv2.cvtColor(img_channel_green, cv2.COLOR_BGR2GRAY)
	result += [result.data.decode() for result in pyzbar.decode(image=img_channel_green)][0]
	# decode blue color channel:
	img_channel_blue = img.copy()
	img_width = img_channel_blue.shape[1]
	img_height = img_channel_blue.shape[0]
	for rows_index in range(img_height):
		for cols_index in range(img_width):
			img_channel_blue[rows_index][cols_index][1] = img_channel_blue[rows_index][cols_index][0]
			img_channel_blue[rows_index][cols_index][2] = img_channel_blue[rows_index][cols_index][0]
	img_channel_blue = cv2.cvtColor(img_channel_blue, cv2.COLOR_BGR2GRAY)
	result += [result.data.decode() for result in pyzbar.decode(image=img_channel_blue)][0]
	return result


# connect to the challenge for the sample data:
conn = remote(host, port)
# read the intro
print(conn.recvuntil(b'> ').decode(), end='')
# request the sample data
option = '0'
conn.writeline(option.encode())
print(option)
# read sample data:
data = conn.readline().decode()
conn.close()
print(data)
data = b64decode(data.split(': ')[1])
# creating the cv image
nparr = np.frombuffer(data, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
result = decode_img(img)
# print the result:
print(result)


# connect to the challenge for the actual challenge data:
conn = remote(host, port)
# read the intro
intro = conn.recvuntil(b'> ').decode()
num_qrcodes = int(intro.split(' ')[3])
print(intro, end='')
# request the sample data
option = '1'
conn.writeline(option.encode())
print(option)
for _ in range(num_qrcodes):
	# read data:
	data = conn.readline().decode()
	print(data)
	data = b64decode(data.split(': ')[1])
	# creating the cv image
	nparr = np.frombuffer(data, np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	result = decode_img(img)
	# print the result:
	print(conn.recvuntil(b'> ').decode(), end='')
	conn.writeline(result.encode())
	print(result)
# read and print the epilog
print(conn.readline().decode())
print(conn.readline().decode())
conn.close()
