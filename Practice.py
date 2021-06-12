# print function
# print('Revision Of Python')

# input function
# name = input('Name: ')
# print(name)

# list
# x = [1, 20, 3, 22, 44, ]
# print(type(x))
# print(x[1])

# for loop
# for i in range(10, 50, 2):
#     i+3
#     print(i)


# Conditionls
# 1.x = 9
# y = 10
# result = x >= 10
# print((result))

# 2.x = 3
# y = 5
# z = 0
# (result1) = (x == y)
# print(result1)

# input function
# num = input('Number: ')
# print(int(num)-5)

# For uppercse
# hello = "hi"
# print(hello.upper())

# # to find the no. of letter
# hello = "Doctor"
# print(hello.count("o"))


# Addition of two string
# x = "hello"
# y = "hii"
# print(x + y)

# if else
# x = input('Please enter ur name ')
# if (x == 'Sunny'):
#     print("You!!")
# else:
#     print('i')

# list
# x = [4, True, "hi"]
# # x.pop(1)
# x.append(2)
# print(x)


# today = "Saturday"
# print(today.upper())
# print(today.capitalize())
# print(today.lower())

# greeting = "Hello"
# Name = "Ashish"
# print(greeting+Name)
# print(greeting+" "+Name + " " "Welcome there")

# def print_full_name(first, last):
#     return first+last


# print(print_full_name(first="Goldu", last="Srivastav"))

# .format()

# find the total for 12 items that weight 3pounds
# weight = 3
# print(weight)
# numitems = 12
# print(numitems)
# if weight < 1:
#     price = 1.45
# if weight >= 1:
#     price = 1.15
#     print(price)
# total = weight*price
# if numitems >= 10:
#     total = total*0.9
# print(total)
# x = 3
# if (x > 2):
#     x = x*2
#     print(x)
# if (x > 4):
#     x = 0
#     print(x)
# print(x)
# Expaltion :- here it first check that x>2 yes it is greater then it multiply it with 2 hence x=6 again in another condition it check if x is greater then 4 and fpund from 4 that it is greater so it is equal to 0
# i = 1
# while True:
#     if i % 007 == 0:
#         break
#     print(i)
#     i += 1
# False

# # Lists
# fruits = ["Orange", "Apple", "Banana"]
# fruits.append("Watermelon")
# fruits.pop(1)
# fruits.insert(4, "Orange")
# fruits.remove("Orange")
# fruits.reverse()
# print(fruits)
# print(len(fruits))
# print(fruits[-1])
# print(fruits)
# # We can add two List  using + operator
# # copy is used to copy list

# # Tuple :- they cannot be modified once they made.. Same like list instead we use ()
# tuple = ("aplle", "Car")
# print(tuple)

# Dictionary
Person1 = {
    "Name": "Ashish",
    "sex": "Male",

}
# print(type(Person1))
# print(Person1["Name"])

# print(Person1.keys())
# Person1["address"] = "1,44 lane"
# # Person1.values
# print(Person1)

# While Loops
# # % % time
# result = 1
# i = 1
# while (i <= 100):
#     result = result*i
#     i = i+1
#     print(result)

# print(f'the factorial of 100 is {result}')
# break Statement
# result = 1
# i = 1
# while i <= 100:
#     result = result*i
#     if i == 42:
#         print(i)
#         break

# print("i=", i)


# To Convert int to binary
# num = 0b11001+0b1010
# print(bin(num)[2:])
# print(int(num))

# Function:- reuseful sets of instruction

# def say_hello(name):
#     print(f'Namaste {name}')


# say_hello('Ashish')
# say_hello('Ashish')
# say_hello('Ashish')

# import math


# def loan_emi(amount):
#     emi = amount/12
#     print(emi)


# print(emi) it gives Error because it is local variable (they Can only use in fucntion) Same as with the amount and also due to Scope Chaining
# loan_emi(126e6)


# def loan_emi(amount, duration, rate, down_payment):
#     loan_amount = amount-down_payment
#     emi = loan_amount*rate * ((1+rate)**duration)/(((1+rate)**duration))
#     emi = math.ceil(emi)
#     return(emi)


# emi1 = loan_emi(amount=1260000, duration=10*12, rate=0.1/12, down_payment=3e5)
# emi2 = loan_emi(amount=1260000, duration=8*12, rate=0.1/12, down_payment=3e5)
# print(emi1)
# print(emi2)
# print("Diffrence in Emi is", emi2-emi1)

# Q>>>cost_of_house=800000
# home_loan_duration=6*12
# home_downpayment=.25*800000
# home_loan_rate=.07/12


# Try and Except
# try:
#     print("Now Computing the Result")
#     result = 5/0
#     print("Computation Was Completed")
# except ZeroDivisionError:
#     print("Failed to divide")

# num = 0b00011001+0b11111001
# print(bin(num))
# print(int(num))
