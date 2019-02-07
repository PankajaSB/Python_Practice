
"""
This program is to generate a random number and ask the user to guess the number and print appropriate message
"""

import random
x = random.randint(0,10)
print(x)


user_guess = int(input("Enter your guess\n"))


while user_guess != x:
    
    if x-1 <= user_guess <= x+1:
        print("You are very close")
    elif user_guess < x:
        print("Guess little higher")
    else:
        print("Guess little lower")
    user_guess = int(input("Enter your guess\n"))

if user_guess == x:
        print("You are correct")