# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# a = float(weight)
# b = float(height)
# print(int(a/(b**2)))

# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# left_age=90-int(age)
# left_weeks=52*left_age
# print(f"You have {left_weeks} weeks left.")
# a = int("5") / int(2.7)
# print(a)
#project2 tip canculator
print('Welcome to the tip canculator.')
bill=input('what was the total bill? $')
percentage=input('what percentage tip would you like to give? 10, 12 or 15 ')
people=input('How many people to split the bill?  ')
a=float(bill)*float(percentage)/100+float(bill)
b=a/int(people)
print(f"Each person should pay: {b} $")