#!/usr/bin/python3

import time
import random
import string

# All these values and functions are meant to be hidden from you by default!
from hidden import sample_data_label, num_chars_per_qrcode, generate_qrcode, challenge_success_label

# Constants:
num_qrcodes = 10
time_limit_in_seconds = 2 * num_qrcodes # The time limit for the challenge-part
alpha_numerics = string.digits + string.ascii_lowercase + string.ascii_uppercase

def request_sample_data():
	'''
	Returns a sample QRCode, which you are supposed to use to demystify the encoding algorithm.
	'''
	sample_data_bytes = generate_qrcode(sample_data_label)
	print(f'Try to uncover the encoding scheme. Once you\'ll succeed, it\'ll be obvious to you! Here is your sample qr code: {sample_data_bytes}')

def start_challenge():
	'''
	Run the challenge.
	'''
	start_time = time.time()
	for count in range(num_qrcodes):
		label = ''.join(random.choices(alpha_numerics, k = num_chars_per_qrcode))
		img = generate_qrcode(label)
		print(f'QRCode #{count + 1}: {img}')
		response = input('> ')
		# check time constraint
		end_time = time.time()
		duration_in_seconds = end_time - start_time
		if duration_in_seconds > time_limit_in_seconds:
			print('You have been too slow. Try again, once you have improved you skills.')
			return
		# check correctness of the captcha value
		if response.strip().lower() != label.lower():
			print('You failed to solve this QRCode. Try again, once you have improved you skills.')
			return
	print(f'It took you {duration_in_seconds} seconds to solve the challenge.')
	print(challenge_success_label)

def main():
	print(f'Can you solve {num_qrcodes} captchas in {time_limit_in_seconds} seconds? You\'ll receive base64 encoded images and you\'ll have to reply with the string represendation of the contained data! Start out with the sample data to verify your script and then attempt to solve the challenge afterwards!')
	print('Options:')
	print('[0] Request sample data.')
	print('[1] Start the challenge.')
	print('[*] Enter anything else to exit immediately.')
	choice = input('> ')
	if choice == '0':
		request_sample_data()
	elif choice == '1':
		start_challenge()
	print("Bye, bye.")

if __name__ == '__main__':
	main()
