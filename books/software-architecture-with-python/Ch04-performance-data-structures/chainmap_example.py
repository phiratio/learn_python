# Code Listing #10

"""

Example of using ChainMap
Here are some practical uses of a ChainMap:

A programmer can keep the GET and POST arguments of a web framework in separate dictionaries and keep the configuration
updated via a single ChainMap.
Keeping multilayered configuration overrides in applications.
Iterating over multiple dictionaries as a view when there are no overlapping keys.
A ChainMap class keeps the previous mappings in its maps attribute. However, when you update a dictionary with mappings
from another dictionary, the original dictionary state is lost.
"""

from collections import ChainMap

d1 = {i: i for i in range(100)}
d2 = {i: i * i for i in range(100)}
c = ChainMap(d1, d2)
# Older value still accessible
print(c[5])
print(c.maps[0][5])
# Updating d1 with d2
d1.update(d2)
print(d1)
# Old value got updated
print(c[5])
print(c.maps[0][5])
