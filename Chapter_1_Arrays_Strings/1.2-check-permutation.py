""" 1.2 Check Permutation: Given two strings, 
write a method to decide if one is a permutation of the other. 
"""

def isPermutation(str1, str2):
	if len(str1) != len(str2):
		print "is NOT permutation"
		return False
	else:
		print "is permutation"
		return ''.join(sorted(str1)) == ''.join(sorted(str2))

if __name__ == '__main__':
	isPermutation('abc','cab')
