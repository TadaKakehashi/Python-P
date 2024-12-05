"""WAP to ask the user to enter names of their 3 names and store them in a list"""

name1 = input("Enter name1:")
name2 = input("Enter name2:")
name3 = input("Enter name3")

lists= [name1, name2, name3]
print(lists)
print(type(lists))

"""WAP to check if a list contains a palindrome of elements"""
list1 =[1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")