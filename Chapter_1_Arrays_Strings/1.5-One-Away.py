""" 1.5 One Away: There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character. Given two strings,
write a function to checke if they are one edit (or zero edits) away
Example:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false

@TODO - not finished yet, needs to be fixed
"""

def isOneEditAway(str1, str2):
	str1 = list(str1)
	str2 = list(str2)

	if str1 == str2:
		print 'strings are the same'
		return True
	elif len(str1) == len(str2):
		print 'replace'
		return isReplace(str1, str2)
	elif len(str2) == len(str1) + 1:
		print 'is delete'
		return isDelete(str1, str2)
	elif len(str2) == len(str1) - 1:
		print 'is add'
		return isAdd(str1, str2)
	else:
		return False

# def isReplace(str1, str2):

# def isDelete(str1, str2):

# def isAdd(str1, str2):	
