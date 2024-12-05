"""Lists: A built-in data type that stores set of values""" 
"""It can store elements of different types float,int,string"""

marks = [94.2,91.1,23.1,55.32,69.69]
print(marks , type(marks))
print(marks[3] + marks[2])
print(len(marks))

#Strings are immutable in Python (Cant be changed)
"""Lists are mutable in Python (Can be changed)"""
student1 = ["Aryan", 95.2, 19, "Bhubaneswar"]
print(student1, type(student1))

#str = "hello"
#str[0] = "a" # is not possible as Strings are immutable 

student1[0] = "Ray"
print(student1) 

"""List Slicing""" #Ending index is not included
print(marks[2:len(marks)])
print(marks[-3:-1])

"""List Methods"""

nums = [2,1,3]

nums.append(4)
print(nums)

nums.sort()
print(nums)


#STRING SORTING
lists = ["banana","apple", "pineapple"]
lists.sort()
print(lists)
lists.sort(reverse=True)
print(lists)


nums.sort(reverse=True)
print(nums)

nums.reverse()
print(nums)
nums.reverse()
print(nums)

#insert method
nums.insert(0,10)
print(nums)
lists.insert(0,"rose")
print(lists)

#remove : remove the first occurrence of the element
nums.remove(10)
print(nums)

#pop : remove the element from its index value
nums.pop(0)
print(nums)

print("TUPLE START")
"""Tuples : A built in Data type that lets us create immutable sequences of values"""
"""Lists are mutable and tuples are immutable"""

tup = (10,20,30,40,50,70)
print(tup[0])
print(tup[1])

#tup[0] = 20 is not possible

#empty tuple:
tup = ()
tups = (1,) #Single value with comma is compulsory
print(tup)
print(type(tup))

#tuple slicing:
tup = (10,20,30,40,50,70)
print(tup[0:3])

#Tuple methods

tup = (2,1,3,1)
print(tup.index(1)) #Returns index of first occurrence
print(tup.count(1)) #Returns the total number of occurrences