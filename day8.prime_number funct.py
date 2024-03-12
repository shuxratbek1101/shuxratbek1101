# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:03:52 2024

@author: user
"""

# Write your code below this line 👇
def prime_checker(number):
  flag=True
  for i in range(2,number):
    if number%i==0:
      flag=False
  if flag:
    print(f"It's a prime number.")
        
  else:
    print(f"It's not a prime number.")
      


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)