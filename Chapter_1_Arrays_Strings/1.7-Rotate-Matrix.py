""" 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Ca you do this in place?

time complexity: n^2, where n is the firs n of matrix definition, 
2 for loops looping through the entire input matrix for each elemeent

Basically, what happens is you got down each row, but backwards on items in each row
"""

from copy import deepcopy

def rotateMatrix(matrix, n):
	new_matrix = deepcopy(matrix) # res will be our original matrix rotate by 90 degrees
	new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

	# x - row index, keeps track of rows, starting from the first one (top one) and going down
	# x - loop through each row from top to bottom, left to right
	for x in range(0, n):  # start: 0, end: 2 (n not inclusive), increment by 1 (by default)
		# y - reverse row index
		# y - loop through each row from bottom to top, right to left
		i = 0  # index for item in each sub-list of new matrix
		for y in range(n-1, -1, -1):   # start: 2, end: 0 (-1 not inclusive), increment by -1 (decrement)
			new_matrix[x][i] = matrix[y][x]
			i += 1

	return new_matrix


if __name__ == '__main__':
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	# [1,2,3]
	# [4,5,6]
	# [7,8,9]

	new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	# new_ma = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
	# [7, 4, 1]
	# [8, 5, 2]
	# [9, 6, 3]

	n = len(matrix)  # n is number of 'rows' in a matrix
	print "Length: ", n
	print "Original matrix: " + str(matrix)
	print "Rotated matrix: " + str(rotateMatrix(matrix, n))
