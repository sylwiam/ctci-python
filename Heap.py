import math
from cStringIO import StringIO
import heapq

def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print output.getvalue()
    print '-' * total_width
    print
    return

data = [19, 9, 4, 10, 11, 8, 2]
print 'data    :', data
heapq.heapify(data)
print 'heapified :'
show_tree(data)
print

inorder = []
while data:
    smallest = heapq.heappop(data)
    print 'pop    %3d:' % smallest
    show_tree(data)
    inorder.append(smallest)
print 'inorder   :', inorder
