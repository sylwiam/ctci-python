""" 10.3 Search in Rotated Array
@TODO - fix, something is not working correclty
"""

def search(l, x, firstIdx, lastIdx):
	midIdx = (firstIdx + lastIdx) / 2
	midEl = l[midIdx]
	firstEl = l[firstIdx]
	lastEl = l[lastIdx]	
	print "firstEl: ", firstEl
	print "midEl: ", midEl
	print "lastEl: ", lastEl

	if midEl == x:  # mid element is x
		return midIdx
	elif firstEl < midEl:  # left side is ordered correctly
		print "firstEl < midEl"
		if x >= firstEl and x < midEl:  # x is in left half, search again
			print "x in left"
			return search(l, x, firstIdx, midIdx - 1 )  # search left
		else:
			print "x in right"
			print "midIdx + 1: ", midIdx + 1
			print "lastIdx: ", lastIdx
			return search(l, x, midIdx + 1, lastIdx)  # search left
	elif firstEl > midEl:  # right side is ordered correctly
		print "firstEl > midEl"
		if x > midEl and x <= lastEl:  # x is in left half, search again
			print "x in left"
			return search(l, x, midIdx + 1, lastIdx)  # search left
		else:
			print "x in right"
			return search(l, x, firstIdx, midIdx - 1)  # search right
	elif firstEl == midEl:  # special case, left half is all repeats
		if firstEl == x:
			return firstIdx
		else:
			return 'Not found'


# l = [10, 15, 20, 0, 5]
l = [10, 15, 20, 0, 5]
# l = [50, 5, 20, 30, 40]

if __name__ == '__main__':
	print search(l, 5, 0, len(l)-1);
