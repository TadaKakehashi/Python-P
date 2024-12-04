#String is data type that stores a sequence of characters

str1 = "This is a string"
str2 = 'Aryan'
str3 = """This is a string"""

str4 = 'this is a string "hi"'

#Escape sequence character
str5 ="this is a string. \n hello \t hello world"
print(str5)

#Concatenation of Strings
str6 = "Nike"
str7 ="Adidas"
print(str6 +"\t"+ str7)

#length of str 
#len(str)

print(len(str6))

#Indexing [character gets a position ]
print(str1[0])

#Slicing of Strings:
#str[starting_idx : ending_idx] ending_idx is not included
print(str6[0:3])
print(str7[2:len(str7)])
print(str7[1:]) #not necessarily we have to write the index number

#Negative index: Special feature in py, we can count our index from starting till end
str8 = "Apple"
print(str8[-4:-1])

#String Functions: 
#1 str.endswith("er") //SubString: if it ends with "er" then it returns true otherwise false.
str1 = "hayabusa"
print(str1.endswith("sa"))

#2 Capitalize Function: 
print(str1.capitalize()) #it creates a new string and the original string remains the same

#3 Replace Function:
print(str1.replace("a","o"))
print(str1.replace("hayabusa", "zx10R"))

#4 Returns First index of 1st occurrence of the word (returns -1 when we enter a word/character which aint in the string)
print(str1.find("a")) #returns index of first occurrence of the word "o"

#5 Count Function
print(str1.count('a'))