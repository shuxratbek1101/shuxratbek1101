# # -*- coding: utf-8 -*-
# """
# Created on Thu Mar  7 16:11:47 2024

# @author: user
# """

# import random
# int_numbers=random.randint(0, 1)
# if int_numbers==0:
#     print('Tails')
# if int_numbers==1:
#     print('Heads')
#=============================================================================
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[0][3])
#=============================================================================
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇


# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# if position.lower()=='a1':
#     map[0][0]='X'
# if position.lower()=='b1':
#     map[0][1]='X'
# if position.lower()=='c1':
#     map[0][2]='X'

# if position.lower()=='a2':
#     map[1][0]='X'
# if position.lower()=='b2':
#     map[1][1]='X'
# if position.lower()=='c2':
#     map[1][2]='X'
    
# if position.lower()=='a3':
#     map[2][0]='X'
# if position.lower()=='b3':
#     map[2][1]='X'
# if position.lower()=='c3':
#     map[2][2]='X'
# print(f"{line1}\n{line2}\n{line3}")
#=============================================================================
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # Your code below
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
# print(f"{line1}\n{line2}\n{line3}")
#==============================================================================
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = int(input("what do you choose? Type 0 for Rock, 1for Paper, 2 for Scissors.\n>>>"))
computer_choice=random.randint(0, 2)
RPS=[rock,paper,scissors]
if user_choice==0:
    print(rock)
if user_choice==1:
    print(paper)
if user_choice==2:
    print(scissors)
if user_choice<0  or user_choice>=3:
    print('You entered an invalid number.\nYou lose')
print(" Computer chose:")
if computer_choice==0:
    print(rock)
if computer_choice==1:
    print(paper)
if computer_choice==2:
    print(scissors)

if computer_choice==0 and user_choice==0:
    print("Draw")
if computer_choice==0 and user_choice==1:
    print("You win")
if computer_choice==0 and user_choice==2:
    print("You lose")
if computer_choice==1 and user_choice==0:
    print("You lose")
if computer_choice==1 and user_choice==1:
    print("Draw")
if computer_choice==1 and user_choice==2:
    print("You win")
if computer_choice==2 and user_choice==0:
    print("You win")
if computer_choice==2 and user_choice==1:
    print("You lose")
if computer_choice==2 and user_choice==2:
    print("Draw")





    