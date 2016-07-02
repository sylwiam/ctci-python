""" 1.6 String Compression: Implement a method to performbasic string compression using the counts
of repeated characters. For eample, the string aabcccccaaa would become a2b1c5a3. If the 'compressed' string 
would not become smaller than the original string, your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a-z) (A-Z).
"""

def compressString(str1):
	res = []
	count = 0
	prev = str1[0]

	for char in str1:
		print "char: ", char
		if char == prev:
			count += 1
		else:
			res += prev + str(count)
			prev = char
			count = 1

	res += prev + str(count)

	res = ''.join(res)

	if len(res) > len(str1):
		return str1
	else:
		return res


print compressString('aabcccccaaa')
