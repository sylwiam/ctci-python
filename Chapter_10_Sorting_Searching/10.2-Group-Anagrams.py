""" 10.2 Group Anagrams: Write a methong to sort an array of string so that all the aanagrams are next to each other.
"""

def organize_anagrams(wordList):
	dictionary = {}

	for item in wordList:
		itemKey = ''.join(sorted(item))
		dictionary.setdefault(itemKey,[]).append(item)
		print dictionary

	finalList = []
	for key, value in dictionary.items():
		finalList.extend(value)


	print "Final: ", finalList
		

l = ['abba', 'bbaa', 'baab', 'c`at', 'cta', 'act', 'dog', 'god']
organize_anagrams(l)