import numpy as np
import cv2

save_path = "results/"

def upside_down(img):
	data = np.zeros(img.shape, dtype="int32")
	(height, width) = data.shape

	for i in xrange(height):
		data[i, :] = img[height - i - 1, :]

	cv2.imwrite(save_path + "upside_down.jpg", data)

def right_side_left(img):
	data = np.zeros(img.shape, dtype="int32")
	(height, width) = data.shape

	for j in xrange(width):
		data[:, j] = img[:, width - j - 1]

	cv2.imwrite(save_path + "right_side_left.jpg", data)

def diagonally_mirror(img):
	data = img
	(height, width) = data.shape

	for x in xrange(width):
		for y in xrange(x, height):
			temp = data[x, y]
			data[x, y] = data[y, x]
			data[y, x] = temp

	cv2.imwrite(save_path + "diagonally_mirror.jpg", data)

if __name__ == '__main__':
	img = cv2.imread('lena.bmp', 0)
	
	# 1
	upside_down(img)

	# 2
	right_side_left(img)

	# 3
	diagonally_mirror(img)

