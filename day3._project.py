# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:52:08 2024

@author: user
"""

# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# a=weight/(height**2)
# if a<18.5:
#   print(f"Your BMI is {a}, you are underweight.")
# if a>=18.5 and a<25:
#   print(f"Your BMI is {a}, you have a normal weight.")
# if a>=25 and a<30:
#   print(f"Your BMI is {a}, you are slightly overweight.")
# if a>=30 and a<35:
#   print(f"Your BMI is {a}, you are obese.")
# if a>35:
#   print(f"Your BMI is {a}, you are clinically obese.")
#=======================================================
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
small_name1=name1.lower()
small_name2=name2.lower()

soni_t=small_name1.count('t')
soni_r=small_name1.count('r')
soni_u=small_name1.count('u')
soni_e=small_name1.count('e')

soni_t2=small_name2.count('t')
soni_r2=small_name2.count('r')
soni_u2=small_name2.count('u')
soni_e2=small_name2.count('e')
jami_1=soni_t+soni_r+soni_u+soni_e+soni_t2+soni_r2+soni_u2+soni_e2

soni_l=small_name1.count('l')
soni_o=small_name1.count('o')
soni_v=small_name1.count('v')
soni_e=small_name1.count('e')

soni_l2=small_name2.count('l')
soni_o2=small_name2.count('o')
soni_v2=small_name2.count('v')
soni_e2=small_name2.count('e')
jami_2=soni_l+soni_o+soni_v+soni_e+soni_l2+soni_o2+soni_v2+soni_e2

jami=str(jami_1)+str(jami_2)
num=int(jami)

if num<10 or num>90:
    print(f"Your score is {jami}, you go together like coke and mentos.")
if num>40 and num<50:
    print(f"Your score is {jami}, you are alright together.")
if num>=10 and num<=40:
    print(f"Your score is {jami}.")
if num>=50 and num<=90:
    print(f"Your score is {jami}.")
#=============================================================================
print('''' ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')
print('Welcome to Treasure Island.Your mission is to find the treasure.')
way=input("Which way would you like to go? (left/right)")
if way.lower()=='left':
    type=input("You came to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat.Type 'swim' to swim across. ")
    if type.lower()=='wait':
        door=input("You came to the island.There is a house with 3 doors.One red, one blue and one yellow\nWhich color do you choose? ")
        if door.lower()=='red':
            print('You were burned by fire.\nGame over!')
        elif door.lower()=='yellow':
            print('You win!')
        elif door.lower()=='blue':
            print('You were eaten by beats.\nGame over!')

    else:
        print("you were attacked by trout\nGame over.")
else:
    print("You fell into a hole. Game over!")
    