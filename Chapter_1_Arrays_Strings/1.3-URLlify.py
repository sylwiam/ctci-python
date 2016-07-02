""" Write a method to replace all spaces in a string with "%20". 
You may assume that the string has suffivient space at the end to hold the additional characters, 
and that yu are given the "true" lengths of the string.
"""
import re

def urlify(str):
	print "'"+str+"'"
	str = str.strip()
	pattern = r'\s+'
	newStr = re.sub(pattern, '%20', str)
	print "'"+newStr+"'"


if __name__ == '__main__':
	urlify('This is a     test.   ')

