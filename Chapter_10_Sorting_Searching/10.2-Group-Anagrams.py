""" 10.2 Group Anagrams: Write a methong to sort an array of string so that all the aanagrams are next to each other.
"""

def organize_anagrams(wordList):
	dictionary = {}

	for item in wordList:
		itemKey = ''.join(sorted(item))
		dictionary.setdefault(itemKey,[]).append(item)

	finalList = []
	for key, value in dictionary.items():
		finalList.extend(value)

	return finalList
		

if __name__ == '__main__':
	l = ['abba', 'cat', 'cta', 'baab', 'act', 'dog', 'god', 'bbaa']

	print organize_anagrams(l)
