# #IF_ELIF_ELSE
# age = int(input("Enter age: "))
# if(age>=18):
#     print("You are eligible for driving  ")
# elif(age<18):
#     print("You are not eligible for driving ")

#indentation meaning the required spacing (proper spacing)

"""Grade Students based on Marks"""

marks = int(input("Enter your marks: "))
if(marks >= 90):
    print("Your Grade is 'A' ")
elif(90> marks >= 80):
    print("Your Grade is 'B' ")
elif(80> marks >=70):
    print("Your Grade is 'C' ")
else:
    print("Your Grade is 'D' ")

""" WAP to check if a number entered by the user is odd or even"""

num = int(input("Enter number: "))
if(num%2 == 0):
    print(str(num) + "Entered by the user is even")
else:
    print(str(num) + "Entered by the user is odd")  

""" WAP to find the greatest of 3 numbers entered by the user"""

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if(num1 > num2):
    if(num1 > num3):
        print(str(num1) +"Entered is the greatest")
elif(num2 > num1):
    if(num2 > num3):
        print(str(num2)+ "Entered is the greatest")
elif(num3 > num1):
    if(num3 > num2):
        print(str(num3)+ "Entered is the greatest")

"""WAP to check if a number is a multiple of 7 or not"""

number = int(input("Enter the value of number: "))

if(number % 7 == 0):
    print(str(number) +"Is a multiple of 7")
else:
    print(str(number)+ "Is not a multiple of 7")