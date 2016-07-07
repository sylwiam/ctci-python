""" 1.1 Is Unique: Implement an algorith to determine if a string has all unique characters. 
What if you cannot use additional data structure?
"""

def isUnique(str):
	charList = []
	for char in str:
		if char not in charList:
			charList.append(char)
		else:
			print 'NOT unique' 
			return False
	print 'Unique'
	return True

def isUniqueNoDS(str):
    #no data structures
    #O(n^2)
    for char in str:
        foundcount = 0
        for char2 in str:
            if char == char2:
                foundcount = foundcount + 1
            if foundcount > 1:
            	print 'NOT Unique'
                return False
	print 'Unique'        
    return True


if __name__ == '__main__':
	isUnique("bacd")


