"""Set is the collection of the unordered items"""
"""Each element in the set must be unique and immutable""" 
"""We cant store list and dictionary in sets because they are mutable"""

collection = {1,2,3,4,5}
print (collection)
print(type(collection))

setcollection = {1,2,2,3,3,4,4,4}
#duplicate values get ignored
print (setcollection)
print(type(setcollection))

#EMPTY SET CREATION: 
collection1 = set()
print (collection1)
print(type(collection1))

#SET METHODS:
"""Sets are mutable but the elements are immutable like the elements cant be changed"""

collection1.add(1)
collection1.add(2)
collection1.add(3)
collection1.add((1,2,3)) #adding a tuple
print (collection1)

#hashable : elements which are immutable that has hash value
#unhashable elements which are mutable and can be changed


collection1.remove(1)
print (collection1)

collection1.clear()
print (len(collection1))

collection2 = {"hello","tada","world"} #it picks elements randomly 
print(collection2.pop())

### Set.union(set2) """combines both set values and returns new"""
set1 ={1,2,3,4,5,6}
set2 = {6,7,8,9,10}
print(set1.union(set2))

###intersetcion : returns common value between two sets
print(set1.intersection(set2))