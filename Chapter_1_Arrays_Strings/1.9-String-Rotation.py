""" 1.9 String Rotation: Assume yu have a method isSubsstring which check is one word is a substring of another. 
Given two strings, s1 and s2, werite code to check if s2 is a rotation of s1 using only one call to isSubstring
(e.g. 'waterbottle' is  arotation of "erbottlewat)

Solution: Concatenate two rotated strings, you'lll see that no matter how you rotate a string, 
the original word is always inside the concatenated one:
"erbottlewat" + "erbottlewat" = "erbottlewaterbottlewat" ("erbottleWATERBOTTLEwat")
"""

def checkRotation(s1, s2):	
	if len(s1) > 0 and (len(s1) == len(s2)):
		s2new = s2 + s2
		print "s2new: ", s2new
		if s1 in s2new:
			return True

	return False

if __name__ == '__main__' :
	# s1 = 'waterbottle'
	# s2 = 'erbottlewat'
	s1 = 'superstorm'
	s2 = 'stormsuper'
	print "s1: ", s1
	print "s2: ", s2
	print checkRotation(s1, s2)


