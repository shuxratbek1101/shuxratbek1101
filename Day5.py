# # -*- coding: utf-8 -*-
# """
# Created on Fri Mar  8 18:09:23 2024

# @author: user
# """

# # Write your code here 👇
# for n in range(1,101):
#     if n%3==0 and n%5==0:
#       n='FizzBuzz'
#     elif n%3==0:
#       n='Fizz'
#     elif n%5==0:
#       n='Buzz'
    
#     print(n)
#==========================================================================
#Password Generator Project
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password=""
# for letter in range(1,nr_letters+1):
#     rand_letter=random.choice(letters)
#     password+=rand_letter

# for symbol in range(1,nr_symbols+1):
#     rand_symbol=random.choice(symbols)
#     password+=rand_symbol

# for number in range(1,nr_numbers+1):
#     rand_number=random.choice(numbers)
#     password+=rand_number
# print(password)
#============================================================================
##Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list=[]
for letter in range(1,nr_letters+1):
    rand_letter=random.choice(letters)
    password_list.append(rand_letter)

for symbol in range(1,nr_symbols+1):
    rand_symbol=random.choice(symbols)
    password_list+=rand_symbol

for number in range(1,nr_numbers+1):
    rand_number=random.choice(numbers)
    password_list+=rand_number
random.shuffle(password_list)
print(password_list)
password=""
for n in password_list:
    password+=n

print(f"Generated code is {password}")




    
