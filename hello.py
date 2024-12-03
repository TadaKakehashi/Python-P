#print is a particular function used to display output in terminal
print("hello" , "world" , 23, 35+21) 

#Assigning variables
name = "Aryan"
age = 21
price = 10.21

#identifying data types:  Integer, String , Float , Boolean, None (a = None)
age2 = None; #None Type
old = False;
print(type(age2),type(old))

print(type(name),type(age),type(price))

#concatenating
name2 = "Mohanty"
total = name +" "+name2
print(type(total),total)

#print Sum
num1 = 10
num2 = 30
sum = num1 + num2
print(sum, type(sum))

#num swapping
A = 20
B = 30
temp = A
A = B
B = temp

print(type(A),A)
print(type(B),B)

# For Single line Comments
"""
multiline comments
Short Cut: ctrl + forward /
"""
a = 10
b= 2
value = a%b
print(value)
print(a**b) #a^2

#relational operators
print(a==b) 
print(a!=b)
print(a>=b)

#assignment operators
num = 10
#num += 10
num **= 2
print(num)

#Type Conversion{Python automatically does it} /Type Casting {Manually changing}
a = float("2") 
b = 4  # str(b)
sum = a+b #returns float
print(sum)

#input 
"""
input is always a String <class str>
to input number: int(input("Enter a number"))
to input a float: float(input(""))
"""
name = input("Enter ur name:")
print(name)

number1 = int(input("Enter num:"))
number2 = int(input("Enter num2:")) 
print("Sum of num:" +str(number1 + number2))