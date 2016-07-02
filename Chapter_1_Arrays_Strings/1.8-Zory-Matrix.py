""" 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, it's entire
row and column are set to 0.

If you simply loop through the matrix and immediately nullify the row and
column of every zero element, you will eventually have an array with all
elements being zero. This needs to be avoided.
"""

"""
Write an algorithm such that if an element in an MxN matrix is 0, it's entire
row and column are set to 0.

If you simply loop through the matrix and immediately nullify the row and
column of every zero element, you will eventually have an array with all
elements being zero. This needs to be avoided.
"""

# by utilizing a class
class ZeroMatrix:

	def __init__(self, matrix):
		self._matrix = matrix

		self._zero_in_rows = []
		self._zero_in_cols = []

		self._num_of_rows = len(self._matrix)
		self._num_of_cols = len(self._matrix[0])  # we are assuming that it's a valid matric and all rows have the same # of cols, so use the first row for column count


	def set_zeros(self):	    
	    for row in range(0, self._num_of_rows):
	        # print "self._num_of_cols: ", self._num_of_cols
	        for col in range(0, self._num_of_cols):
	            # print "item: ", self._matrix[row][col]
	            if self._matrix[row][col] == 0:
	            	if row not in self._zero_in_rows:
	                	self._zero_in_rows.append(row)
	                if col not in self._zero_in_cols:
	                	self._zero_in_cols.append(col)
	    print "self._zero_in_rows: ", self._zero_in_rows
	    print "self._zero_in_cols: ", self._zero_in_cols
	    # nullify_columns(self._matrix)
	    # nullify_rows(self._matrix)
	    self.nullify_rows_and_cols()
	    print "after:  ", self._matrix, '\n'
	    return self._matrix

	# option 1: nulify columns and rows separately
	def nullify_columns(self):
	    for column in self._zero_in_cols:
	        for row in self._matrix:
	            row[column] = 0

	def nullify_rows(self):
	    for row in self._zero_in_rows:
	        for index in range(0, len(self._matrix[0])):
	            self._matrix[row][index] = 0

	# option 1: nulify columns and rows together, traversing only once through the self._matrix
	def nullify_rows_and_cols(self):
		for row in range(0, self._num_of_rows):
		    # print "self._num_of_cols: ", self._num_of_cols
		    for col in range(0, self._num_of_cols):
		        if row in self._zero_in_rows:
		        	self._matrix[row][col] = 0

		        if col in self._zero_in_cols:
		            self._matrix[row][col] = 0


if __name__ == '__main__' :
	# self._matrix = [[1,0,3,5], [2,5,6,2], [9,3,0,8], [3,4,5,7], [0,8,3,1]]
	matrix = [[0,1,0,2], [2,5,6,1], [9,3,1,8], [3,4,5,7], [9,8,3,1]]
	print "before: ", matrix
	# set_zeros(self._matrix)

	mx = ZeroMatrix(matrix)
	mx.set_zeros()

