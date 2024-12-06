"""Dictionaries are used to store data value in key:value pairs"""
"""They are unordered, mutable(changeable) & dont allow duplicate keys"""
#"key": value

info = {
    "name" : "tada",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict","set"),
    "learning" : "coding",
    "age" : 21,
    "is_adult" : True,
    "marks" : 94.3
}
print(info , type(info))

dict = {
    "name" : "ray",
    "age" : 21,
    "bike" : "GT650"
}

print(dict["name"])
dict["bike"] =  "Kawasaki"
dict["sex"] = "male" #adding new key
print(dict)

#EMPTY DICTIONARY:
null_dict ={}
print(null_dict)


"""Nested Dictionaries"""
student = {
    "name" : "Aryan",
    "studentInfo" : {
        "phy" : 97,
        "maths" :100,
        "java" : 56
    }
}

print(student["studentInfo"])
print(student["studentInfo"]["phy"])

"""Dictionary Methods"""
#1. myDict.keys() returns all the keys of the dictionary
print(len(student)) #total number of keys  
print(list(student.keys())) #returns the keys of the dictionary

#2 myDict.values() returns all the values of the dictionary
print(student.values())

#3 myDict.items() returns all (key,val) pairs as tuples
print(student.items()) 
pairs = list(student.items())
print(pairs[0])

#4 myDict.get("key") returns the key according to value
print(student.get("name")) #If the value ain't in the dic it returns None where as normally it returns an error

"""When errors occurs the whole program stops executing and meanwhile when we use method who doesn't throw any errors it helps in execution of the program"""

#5 myDict.update(newDict) #inserts the specified items to the dictionaries
student.update({"city":"delhi", "drive" : "yes"})
print(student)