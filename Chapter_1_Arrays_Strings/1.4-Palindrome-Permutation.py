""" 1.4 Palindrome Permutation: Given a string, wtie a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrengement of letters. 
The palindrome does not need to be limited to just dictionary words. 
"""

import string

def isPermutationOfPalindrome(str):
	d = dict.fromkeys(string.ascii_lowercase, False) # get all ASCII characters and add them to dictionary as key, default all values to False
	# False in dictionary would mean the number of characters in a string is even
	# True in dictionary would mean the number of characters in a string is odd
	count = 0

	# loop throught each char in string and switch True/False valeu in dict every time you encounter it

	for char in str:
		if (ord(char) > 97 and ord(char) < 123): #98-122 in ASCII are all lowercase characters, make sure your stirng is all lowercase
			d[char] = not d[char]

	for key in d:
		if d[key] is True: # count all characters with odd count (we can have only 1!)
			count += 1
			if count > 1: # if count of odd characters is more than 1, return False
				return False

	return True

if __name__ == '__main__':
	isPermutationOfPalindrome('abc')
